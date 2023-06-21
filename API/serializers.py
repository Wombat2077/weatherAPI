from rest_framework import serializers
from .models import *

class WindSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wind
        fields = "__all__"

class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = "__all__"
class PrecSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Precipitation
        fields = "__all__"
class TempSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Temperature
        fields = "__all__"
class WeatherSerializer(serializers.ModelSerializer):

    place = PlaceSerializer()
    prec = PrecSerializer()
    temp = TempSerializer()
    wind = WindSerializer()
    
    class Meta:
        model = Weather
        fields = "__all__"