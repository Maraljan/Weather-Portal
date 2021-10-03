import requests

from weather.models import CityWeatherInfo
from weather_portal.settings import OPEN_WEATHER_API_KEY, OPEN_WEATHER_URL


class OpenWeatherClient:

    def __init__(self):
        self._api_key = OPEN_WEATHER_API_KEY
        if OPEN_WEATHER_API_KEY is None:
            raise ValueError('Api key not found')
        self._session = requests.Session()

    def get_city_weather(self, city: str) -> dict:
        response = self._session.get(OPEN_WEATHER_URL, params={'q': city, 'appid': self._api_key, 'units': 'metric'})
        result = response.json()
        return result

    @staticmethod
    def parse_weather(weather: dict) -> CityWeatherInfo:
        country_code = weather['sys']['country']
        city_name = weather['name']
        weather_description = weather['weather'][0]['description']
        temp = weather["main"]["temp"]
        temp_feels_like = weather["main"]["feels_like"]
        temp_max = weather["main"]["temp_max"]
        temp_min = weather["main"]["temp_min"]

        return CityWeatherInfo(
            city_name=city_name,
            country_code=country_code,
            weather_description=weather_description,
            temp=temp,
            temp_feels_like=temp_feels_like,
            temp_min=temp_min,
            temp_max=temp_max,
        )


if __name__ == '__main__':
    weather_ = OpenWeatherClient()
    print(weather_.get_city_weather('Kiev'))
