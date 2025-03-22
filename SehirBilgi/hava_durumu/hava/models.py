from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    wind_speed = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)  # Son güncelleme tarihi

    def __str__(self):
        return self.city
