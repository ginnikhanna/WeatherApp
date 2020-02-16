import weatherapiclient
from weatherapiclient import WeatherInfo
import openweather_apiclient
class WeatherService:

    def __init__(self, city,
                 weather_apiclient = openweather_apiclient.OpenWeatherApiClient):
        self._city = city
        self._weatherapiclient = weather_apiclient

    def city(self):
        return self._city

    def get_weather(self):
        weather = self._weatherapiclient.current_weather(self._city)
        if weather.temp_unit is 'celsius':
            return weather
        elif weather.temp_unit is 'kelvin':
            return self._convert_from_kelvin(weather)
        else:
            return self._convert_from_fahrenheit(weather)

    def get_temperature(self):
        return self.get_weather().temp

    def get_temperature_feels_like(self):
        return self.get_weather().feels_like

    def _convert_from_fahrenheit(self, weather :WeatherInfo):
        temp_celsius  = int((weather.temp - 32)/1.8)
        temp_feels_like = int((weather.feels_like - 32)/1.8)
        new_weather = WeatherInfo(temp_celsius,
                           temp_feels_like,
                           weather.temp_min,
                           weather.temp_max,
                           weather.pressure,
                           weather.humidity,
                           'celsius')

        return new_weather

    def _convert_from_kelvin(self, weather: WeatherInfo):
        temp_celsius = int(weather.temp -  273.15)
        temp_feels_like = int(weather.feels_like -  273.15)
        new_weather = WeatherInfo(temp_celsius,
                                  temp_feels_like,
                                  weather.temp_min,
                                  weather.temp_max,
                                  weather.pressure,
                                  weather.humidity,
                                  'celsius')

        return new_weather






