import json

import requests
from requests.exceptions import HTTPError

from weather.models import CityWeatherInfo
from weather_portal.settings import OPEN_WEATHER_API_KEY, OPEN_WEATHER_URL, FORECAST_WEATHER_URL


class OpenWeatherError(Exception):
    """
    Exception for all errors in OpenWeatherAPI.
    """


class OpenWeatherClient:
    """
    Client for OpenWeatherAPI.
    """
    def __init__(self):
        self._api_key = OPEN_WEATHER_API_KEY
        if OPEN_WEATHER_API_KEY is None:
            raise ValueError('Api key not found')
        self._session = requests.Session()

    def get_weather_forecast(self, city) -> list:
        """
        Get Forecast for 5 days with 3 hour step.
        """
        try:
            response = self._session.get(FORECAST_WEATHER_URL, params={'q': city, 'appid': self._api_key, 'units': 'metric'})
        except requests.exceptions.ConnectionError:
            raise OpenWeatherError('Connection with OpenWeatherAPI was failed')
        try:
            response.raise_for_status()
            result = response.json()
        except (json.JSONDecodeError, HTTPError):
            raise OpenWeatherError('Failed to fetch weather')
        forecast_5days = []
        try:
            for weather in result['list']:
                forecasts_current_time = {
                    'temperature': weather['main']['temp'],
                    'description': weather['weather'][0]['description'],
                    'icon': weather['weather'][0]['icon'],
                    'date': weather['dt_txt'][:-3]
                }
                forecast_5days.append(forecasts_current_time)
        except (KeyError, IndexError):
            raise OpenWeatherError('Parsing weather failed.')
        return forecast_5days

    def get_city_weather(self, city: str) -> dict:
        """
        Get current weather.
        """
        try:
            response = self._session.get(OPEN_WEATHER_URL, params={'q': city, 'appid': self._api_key, 'units': 'metric'})
        except requests.exceptions.ConnectionError:
            raise OpenWeatherError('Connection with OpenWeatherAPI was failed')
        try:
            response.raise_for_status()
            result = response.json()
        except (json.JSONDecodeError, HTTPError):
            raise OpenWeatherError('Failed to fetch weather')
        return result

    @staticmethod
    def parse_weather(weather: dict) -> CityWeatherInfo:
        """
        Convert weather json.
        """
        try:
            country_code = weather['sys']['country']
            city_name = weather['name']
            weather_description = weather['weather'][0]['description']
            temp = weather["main"]["temp"]
            temp_feels_like = weather["main"]["feels_like"]
            temp_max = weather["main"]["temp_max"]
            temp_min = weather["main"]["temp_min"]
            icon = weather['weather'][0]["icon"]
        except (KeyError, IndexError):
            raise OpenWeatherError('Parsing weather failed.')

        return CityWeatherInfo(
            city_name=city_name,
            country_code=country_code,
            weather_description=weather_description,
            temp=temp,
            temp_feels_like=temp_feels_like,
            temp_min=temp_min,
            temp_max=temp_max,
            icon=icon,
        )


if __name__ == '__main__':
    weather_ = OpenWeatherClient()
    print(weather_.get_weather_forecast('ashgabat'))

