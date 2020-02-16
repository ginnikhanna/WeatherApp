import weatherapiclient
from weatherapiclient import WeatherInfo


class MockWeatherApiClient(weatherapiclient.WeatherApiClient):

    def __init__(self):
        weatherapiclient.WeatherApiClient.__init__(self)

    def initialize(self, desired_weather_info):
        self._desired = desired_weather_info

    def current_weather(self, city: str) -> WeatherInfo:
        return self._desired
