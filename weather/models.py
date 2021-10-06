from django.db import models


class CityWeatherInfo(models.Model):

    class Meta:
        unique_together = [('city_name', 'date')]

    city_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    country_code = models.CharField(max_length=30)
    weather_description = models.CharField(max_length=30)
    temp = models.FloatField()
    temp_feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    icon = models.CharField(max_length=30)
