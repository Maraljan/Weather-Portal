from django.urls import path
from weather.views import HomePageView, ArchiveView

app_name = 'weather'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('archive', ArchiveView.as_view(), name='archive'),
]
