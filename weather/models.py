from django.db import models


class CityWeatherInfo(models.Model):
    city_name = models.CharField(max_length=30)
    country_code = models.CharField(max_length=30)
    weather_description = models.CharField(max_length=30)
    temp = models.FloatField()
    temp_feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
