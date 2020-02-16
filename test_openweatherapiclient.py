import unittest

import openweather_apiclient
import weatherapiclient
import weatherservice


class MyTestCase(unittest.TestCase):
    def test_return_content_from_api(self):
        o = openweather_apiclient.OpenWeatherApiClient()
        data = o.current_weather('Delhi')
        self.assertIsNotNone(data)

    def test_json_content_from_api_is_a_weather_info_type(self):
        o = openweather_apiclient.OpenWeatherApiClient()
        data = o.current_weather('Delhi')
        self.assertIsInstance(data, weatherapiclient.WeatherInfo)



if __name__ == '__main__':
    unittest.main()
