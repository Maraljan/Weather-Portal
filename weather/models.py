from django.db import models
from django.utils.safestring import mark_safe


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
    icon = models.CharField(max_length=20)

    @property
    def icon_preview(self):
        return mark_safe(f'<img src="http://openweathermap.org/img/w/{self.icon}.png" alt="Image" style="width:60px">')
