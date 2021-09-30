import requests

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
        country_name = result['sys']['country']
        city_name = result['name']
        weather_description = result['weather'][0]['description']
        temp = f'{result["main"]["temp"]}°F'
        feels_like = f'{result["main"]["feels_like"]}°F'
        temp_max = f'{result["main"]["temp_max"]}°F'
        temp_min = f'{result["main"]["temp_min"]}°F'

        return city_name, country_name, weather_description, temp, feels_like, temp_min, temp_max


if __name__ == '__main__':
    weather = OpenWeatherClient()
    print(weather.get_city_weather('Kiev'))
