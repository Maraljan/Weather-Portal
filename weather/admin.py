from django.contrib import admin
from .models import CityWeatherInfo


@admin.register(CityWeatherInfo)
class PostAdmin(admin.ModelAdmin):
    list_display = ('city_name', "show_icon", 'date')
    readonly_fields = ['show_icon']

    def show_icon(self, obj: CityWeatherInfo):
        return obj.icon_preview
