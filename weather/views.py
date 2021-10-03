from django.views.generic import TemplateView, FormView

from weather.forms import CityForm
from weather.services.open_weather_map import OpenWeatherClient


class HomePageView(FormView):

    template_name = 'weather/home_page.html'
    form_class = CityForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client_weather = OpenWeatherClient()

    def form_valid(self, form: CityForm):
        name_city = form.cleaned_data['city']
        raw_weather = self.client_weather.get_city_weather(name_city)
        weather = self.client_weather.parse_weather(raw_weather)
        return self.render_to_response(self.get_context_data(weather=weather))
