from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import WeatherData
from .serializers import WeatherDataSerializer
from unidecode import unidecode

def home(request):
    return render(request, "index.html")

def search_city_weather(request):
    query = request.GET.get('city')
    if not query:
        return redirect('home')  # Eğer bir şehir girilmediyse ana sayfaya yönlendir

    normalized_query = unidecode(query.lower())

    try:
        weather = WeatherData.objects.get(city__iexact=normalized_query)
        return render(request, "city_weather.html", {"weather": weather})
    except WeatherData.DoesNotExist:
        # Tüm veritabanındaki şehir isimlerini normalize ederek arama yap
        all_weather_data = WeatherData.objects.all()
        for weather in all_weather_data:
            if unidecode(weather.city.lower()) == normalized_query:
                return render(request, "city_weather.html", {"weather": weather})
        return render(request, "city_weather.html", {"error": f"No weather data found for {query}"})


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
