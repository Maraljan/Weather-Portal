from django.db import IntegrityError
from django.db.models import QuerySet
from django.utils.dateparse import parse_date
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import FormView, ListView, TemplateView

from utils import add_url_params
from weather.forms import CityForm, ArchiveForm, ForecastForm
from weather.models import CityWeatherInfo
from weather.services.open_weather_map import OpenWeatherClient, OpenWeatherError


class HomePageView(FormView):

    template_name = 'weather/home_page.html'
    form_class = CityForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_weather = OpenWeatherClient()

    def form_valid(self, form: CityForm):
        name_city = form.cleaned_data['city']
        error = None
        weather = None
        try:
            weather = CityWeatherInfo.objects.get(city_name__iexact=name_city, date=timezone.now().date())
        except CityWeatherInfo.DoesNotExist:
            try:
                weather = self._get_weather(name_city)
            except OpenWeatherError:
                error = 'Could not get information about weather.'
        return self.render_to_response(self.get_context_data(weather=weather, error=error))

    def _get_weather(self, city: str) -> CityWeatherInfo:
        raw_weather = self.client_weather.get_city_weather(city)
        weather = self.client_weather.parse_weather(raw_weather)
        try:
            weather.save()
        except IntegrityError:
            pass
        return weather


class ArchiveView(FormView, ListView):

    template_name = 'weather/archive.html'
    form_class = ArchiveForm
    model = CityWeatherInfo
    context_object_name = 'city_weathers'
    paginate_by = 5

    def form_valid(self, form: ArchiveForm):
        """

        """
        response = redirect('weather:archive')
        response['Location'] = add_url_params(response[ 'Location'], form.cleaned_data)
        return response

    def get_queryset(self) -> QuerySet[CityWeatherInfo]:
        queryset = super().get_queryset()
        if city := self.request.GET.get('city'):
            queryset = queryset.filter(city_name__iexact=city)
        if date_to := self.request.GET.get('date_to'):
            queryset = queryset.filter(date__lte=parse_date(date_to))
        if date_from := self.request.GET.get('date_from'):
            queryset = queryset.filter(date__gte=parse_date(date_from))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_params'] = add_url_params('', {
            'city': self.request.GET.get('city'),
            'date_to': self.request.GET.get('date_to'),
            'date_from': self.request.GET.get('date_from'),
        })
        return context


class ForecastView(FormView):
    template_name = 'weather/forecast.html'
    form_class = ForecastForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_weather = OpenWeatherClient()

    def form_valid(self, form: ForecastForm):
        name_city = form.cleaned_data['city']
        weather = self.client_weather.get_weather_forecast(name_city)
        return self.render_to_response(self.get_context_data(weather=weather))
