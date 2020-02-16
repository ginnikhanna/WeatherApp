from flask import Flask, request
import weatherservice
import weatherapiclient
import openweather_apiclient
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Weather information</h1>'

@app.route('/weather', methods = ["GET"])
def weather():
    city = request.args.get('city')
    w = weatherservice.WeatherService(city, openweather_apiclient.OpenWeatherApiClient())
    temp = w.get_temperature()
    feels_like_temp = w.get_temperature_feels_like()

    return f'Temperature in {w.city()} is {temp}°Celcius and it feels like {feels_like_temp}°Celcius'



if __name__ == '__main__':
    app.run(debug='True')