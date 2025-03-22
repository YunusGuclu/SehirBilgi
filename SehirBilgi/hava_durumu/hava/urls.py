from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherDataViewSet, home, search_city_weather

router = DefaultRouter()
router.register(r'weather', WeatherDataViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("search/", search_city_weather, name="search_city_weather"),
    path('api/', include(router.urls)),
]
