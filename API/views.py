from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
import yandex_weather_api
import datetime
import requests

from .models import *
from .serializers import *


class WeatherView(APIView):
    
    def get(self, request):
        latitude = float(request.GET.get('latitude') if request.GET.get('latitude') else 0) 
        longitude = float(request.GET.get('longitude') if request.GET.get('longitude') else 0)
        today = datetime.date.today()
        place = Place.objects.get_or_create(latitude=latitude, longitude=longitude)[0].pk
        try:
            print(type(Weather.objects))
            weather = Weather.objects.get(place=place, date=today)
        except(Weather.DoesNotExist):
            ya_resp = yandex_weather_api.get(requests, settings.YANDEX_API_KEY, lat=latitude, lon=longitude, rate='forecast').to_dict()['fact'] # yandex response - author
            print("n\n\1\n\n")
            temp = Temperature.objects.create(temp=ya_resp.get('temp'), feels=ya_resp.get('feels_like'), water_temp=ya_resp.get('water'))
            prec = Precipitation.objects.create(prec_type=ya_resp.get('prec_type'), prec_strength=ya_resp.get('prec_strength'), cloudness=ya_resp.get('cloudness'))
            wind = Wind.objects.create(speed=ya_resp.get('wind_speed'), direction=ya_resp.get('wind_dir'), gust=ya_resp.get('wind_gust'))
            print("there is bug")
            weather = Weather.objects.create(weather_condition=ya_resp.get('condition'), date=today, temp=temp, place=Place.objects.get(id=place), prec=prec, wind=wind)
        serializer = WeatherSerializer(weather)
        print(serializer.data)
        return Response(serializer.data)
