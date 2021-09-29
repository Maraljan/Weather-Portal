from django.urls import path
from weather.views import HomePageView

app_name = 'weather'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
