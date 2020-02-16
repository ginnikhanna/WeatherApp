import unittest
import mockweather_apiclient
from weatherapiclient import WeatherInfo
import weatherservice

class TestWeatherResults(unittest.TestCase):


    def test_returns_current_weather_given_temp_in_celsius(self):
        expected_weather_info = WeatherInfo(26, 23, 21, 24, 100, 50, 'celsius')
        api_client = mockweather_apiclient.MockWeatherApiClient()
        api_client.initialize(expected_weather_info)
        w = weatherservice.WeatherService('Delhi', api_client)
        self.assertEqual(expected_weather_info, w.get_weather())

    def test_converts_temp_to_celsius_when_getting_temp_in_fahrenheit(self):
        temp_in_fahrenheit = 80
        feels_like_in_fahrenheit = 80
        weather_info = WeatherInfo(temp_in_fahrenheit, feels_like_in_fahrenheit, 21, 24, 100, 50, 'fahrenheit')
        api_client = mockweather_apiclient.MockWeatherApiClient()
        api_client.initialize(weather_info)
        w = weatherservice.WeatherService('Delhi', api_client)

        expected_temp_in_celsius = 26
        expected_weather_info = WeatherInfo(expected_temp_in_celsius, expected_temp_in_celsius, 21, 24, 100, 50, 'celsius')
        self.assertEqual(expected_weather_info, w.get_weather())


    def test_converts_temp_to_celsius_when_getting_temp_in_kelvin(self):
        temp_in_kelvin = 273
        feels_like_in_kelvin = 273
        weather_info = WeatherInfo(temp_in_kelvin, feels_like_in_kelvin, 21, 24, 100, 50, 'kelvin')
        api_client = mockweather_apiclient.MockWeatherApiClient()
        api_client.initialize(weather_info)
        w = weatherservice.WeatherService('Delhi', api_client)

        expected_temp_in_celsius = 0
        expected_feels_like_in_celsius = 0

        expected_weather_info = WeatherInfo(expected_temp_in_celsius, expected_feels_like_in_celsius, 21, 24, 100, 50, 'celsius')
        self.assertEqual(expected_weather_info, w.get_weather())


    def test_returns_temperature_in_celcius(self):
        expected_temp_in_celsius = 23
        expected_weather_info = WeatherInfo(expected_temp_in_celsius, 23, 21, 24, 100, 50, 'celsius')
        api_client = mockweather_apiclient.MockWeatherApiClient()
        api_client.initialize(expected_weather_info)
        w = weatherservice.WeatherService('Delhi', api_client)

        self.assertEqual(expected_temp_in_celsius, w.get_temperature())

if __name__ == '__main__':
    unittest.main()
