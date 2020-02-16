from collections import namedtuple

WeatherInfo = namedtuple('WeatherInfo', ['temp',
                                  'feels_like',
                                  'temp_min',
                                  'temp_max',
                                  'pressure',
                                  'humidity',
                                  'temp_unit'])


class WeatherApiClient:

    def __init__(self):
        pass

    def current_weather(self, city:str) -> WeatherInfo:
        ''' Returns the temperature of the city'''
        raise Exception("NotImplementedException")



