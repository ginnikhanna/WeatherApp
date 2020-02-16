import json
import urllib.request

import secret
import weatherapiclient
from weatherapiclient import WeatherInfo


class OpenWeatherApiClient(weatherapiclient.WeatherApiClient):

    def __init__(self):
        weatherapiclient.WeatherApiClient.__init__(self)

    def current_weather(self, city: str):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={secret.api_key}'
        data = urllib.request.urlopen(url).read()
        data = json.loads(data)

        return self._to_weather_info(data)

    def _to_weather_info(self, data: json) -> WeatherInfo:
        return WeatherInfo(data['main']['temp'],
                           data['main']['feels_like'],
                           data['main']['temp_min'],
                           data['main']['temp_max'],
                           data['main']['pressure'],
                           data['main']['humidity'],
                           'kelvin')


class AccuWeatherApiClient(weatherapiclient.WeatherApiClient):
    def __init__(self):
        pass

    def current_weather(self, city):
        raise Exception("NotImplementedException")
