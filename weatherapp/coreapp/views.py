from django.shortcuts import render
import requests 
from django.shortcuts import render
import datetime

def index(request):
    API_KEY = open("API_KEY", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,hourly,minutely,hourly,alerts&appid={}"
    
    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.get['city2', None]
    else:
        return render()
    


def featch_forecast(city, api_key, current_weather_url, forecast_url):
    
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response ['coord']['Lon']
    
    forecast_response = requests. get (forecast_url. format (lat, lon, api_key)).json()
    
    
    weather_data = {
            "city": city,
            "temperature": round(response ['main' ]['temp'] - 273.15, 2),
            "description": response ['weather'][0] ['description'],
            "icon": response['weather'][0]['icon']
    }
    
    daily_forecasts = []
    for daily_data in forecast_response ['daily'][:5]:
        daily_forecasts.append ({
            "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            "min_temp": round(daily_data['temp']['min'] - 273.15, 2),
            "max_temp": round(daily_data['temp']['max'] - 273.15, 2),
            "description": daily_data['weather'][0] ['description'],
            "icon": daily_data['weather'][0]['icon']
        })