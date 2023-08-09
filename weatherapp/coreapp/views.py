from django.shortcuts import render
import requests 
from django.shortcuts import render
import datetime

def index(request):
    API_KEY = '4e86a244f2390ce5f67c7cd1b533ee69'
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,hourly,minutely,hourly,alerts&appid={}"

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2')  # Use get() method to handle None case
        
        weather_data1, daily_forecasts1 = fetch_forecast(city1, API_KEY, current_weather_url, forecast_url)
        
        weather_data2, daily_forecasts2 = None, None  # Initialize variables
        
        if city2:  # Check if city2 is not None
            weather_data2, daily_forecasts2 = fetch_forecast(city2, API_KEY, current_weather_url, forecast_url)

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2
        }

        return render(request, "index.html", context)
        
    else:
        return render(request, "index.html")
    


def fetch_forecast(city, api_key, current_weather_url, forecast_url):
    
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response ['coord']['lon']
    
    forecast_response = requests.get(forecast_url.format(lon, lat, api_key)).json()
    
    
    weather_data = {
            "city": city,
            "temperature": round(response ['main' ]['temp'] - 273.15, 2),
            "description": response ['weather'][0] ['description'],
            "icon": response['weather'][0]['icon']
    }
    
    daily_forecasts = []
    for daily_data in forecast_response["daily"][:5]:
        daily_forecasts.append ({
            "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            "min_temp": round(daily_data['temp']['min'] - 273.15, 2),
            "max_temp": round(daily_data['temp']['max'] - 273.15, 2),
            "description": daily_data['weather'][0] ['description'],
            "icon": daily_data['weather'][0]['icon']
        })
        
    return weather_data, daily_data