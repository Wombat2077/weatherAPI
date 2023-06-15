from django.db import models

class Place(models.Model):
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")
    #name = models.CharField("name", max_length=100, null=True, default='')
    
class Wind(models.Model):
    speed = models.FloatField("speed", default=0)
    direction = models.CharField("direction", max_length=2, default="c") # возможные значения направления -  n ne e se s sw w nw c
    gust = models.FloatField("gust", default=0)
    
class Temperature(models.Model):
    temp = models.FloatField("temp")
    feels = models.FloatField("feels_like")
    water_temp = models.FloatField("water_temp")

class Precipitation(models.Model):
    prec_type = models.PositiveSmallIntegerField("type")
    prec_strength = models.FloatField("strength", default=0)
    cloudness = models.FloatField("cloudness", default=0)
    
class Weather(models.Model):
    weather_condition = models.CharField("condition", max_length=30)
    date = models.DateField("date")
    temp = models.ForeignKey(Temperature, on_delete=models.SET_NULL, null=True)
    prec = models.ForeignKey(Precipitation, on_delete=models.SET_NULL, null=True)
    wind = models.ForeignKey(Wind, on_delete=models.SET_NULL, null=True)
    #place = models.ForeignKey(Place, on_delete=models.SET_DEFAULT, default=Place.objects.get(id=1).pk)