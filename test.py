import yandex_weather_api
import requests
import pprint

req = requests
pprint.pprint(yandex_weather_api.get(req, "39928290-6b4b-49dc-9f90-d085e6ea7a10", rate='forecast', lat=55.10, lon=60.10).to_dict())
