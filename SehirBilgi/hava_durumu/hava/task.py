# tasks.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
from .models import WeatherData

API_KEY = 'c45966f73686cf713980007192a3b8aa'
cities = [
    'Adana', 'Adıyaman', 'Afyonkarahisar', 'Ağrı', 'Aksaray', 'Amasya', 'Ankara', 'Antalya', 'Ardahan',
    'Artvin', 'Aydın', 'Balıkesir', 'Bartın', 'Batman', 'Bayburt', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur',
    'Bursa', 'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Düzce', 'Edirne', 'Elazığ', 'Erzincan',
    'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Iğdır', 'Isparta', 'İstanbul',
    'İzmir', 'Kahramanmaraş', 'Karabük', 'Karaman', 'Kars', 'Kastamonu', 'Kayseri', 'Kırıkkale', 'Kırklareli', 'Kırşehir',
    'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa', 'Mardin', 'Mersin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu',
    'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Şanlıurfa', 'Şırnak', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Uşak',
    'Van', 'Yalova', 'Yozgat', 'Zonguldak'
]

def fetch_weather_data(city="Elazig"):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr'
    response = requests.get(URL)
    if response.status_code == 200:
        weather_data = response.json()
        weather, created = WeatherData.objects.update_or_create(
            city=weather_data['name'],
            defaults={
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'wind_speed': weather_data['wind']['speed'],
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
                'temperature_min': weather_data['main']['temp_min'],
                'temperature_max': weather_data['main']['temp_max'],
                'visibility': weather_data['visibility'],
                'cloudiness': weather_data['clouds']['all'],
                'sunrise': weather_data['sys']['sunrise'],
                'sunset': weather_data['sys']['sunset'],
            }
        )
        if created:
            print(f"Weather data created for {city}")
        else:
            print(f"Weather data updated for {city}")
    else:
        print(f"Failed to fetch weather data for {city}: {response.status_code}")

def update_all_weather_data():
    for city in cities:
        fetch_weather_data(city)

scheduler = BackgroundScheduler()
scheduler.add_job(update_all_weather_data, IntervalTrigger(minutes=5))
scheduler.start()
