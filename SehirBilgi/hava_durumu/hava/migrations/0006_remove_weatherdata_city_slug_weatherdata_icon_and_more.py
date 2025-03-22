# Generated by Django 5.0.8 on 2024-08-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hava", "0005_remove_weatherdata_icon_weatherdata_city_slug_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weatherdata",
            name="city_slug",
        ),
        migrations.AddField(
            model_name="weatherdata",
            name="icon",
            field=models.CharField(default="default_icon.png", max_length=255),
        ),
        migrations.AlterField(
            model_name="weatherdata",
            name="city",
            field=models.CharField(max_length=255),
        ),
    ]
