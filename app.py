from flask import Flask, render_template, request
import flask
import requests
app=flask.Flask(__name__)
API_KEY ='0215cd2355fcb8aff6980538ba5a6895'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()

    else:
        return None

def parse_weather_data(data):
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']     
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return {
       'city':data['name'],
       'temperature':data['main']['temp'],
       'description':data['weather'][0]['description'],
       'humidity':data['main']['humidity'],
       'wind_speed':data['wind']['speed']
    }
@app.route('/',methods=['GET','POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        data = fetch_weather(city)
        if data:
            weather_data = parse_weather_data(data)
    return render_template('index.html', weather=weather_data)
if __name__=='__main__':
    app.run(debug=True)
    