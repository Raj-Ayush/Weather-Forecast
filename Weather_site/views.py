# Created by self.
import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    # for accessing current date and time.------------
    today = datetime.date.today()
    current = datetime.datetime.now()
    time = current.strftime("%I:%M %p")
    d2 = today.strftime("%B %d, %Y")
    date = {
        'Date':d2,
        'time':time
    }
    context = {'dateTime': date}
    # ------------------------------------------------
    return render(request,'index.html',context)

def result(request):
    city = request.POST.get('text','default')
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=3f745532c2de8e69e54dbe27b4bdbcfc'

    url= "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=QWHdOA7gcUMcVn14tDnhh4BJCtFmRkzT&q={}&language=en-us&offset=1"
    k = requests.get(url.format(city)).json()

    r = requests.get(url1.format(city)).json()
    celsius = round(r['main']['temp'] - 273,1)

#for accessing current date and time.------------
    today = datetime.date.today()
    current = datetime.datetime.now()
    time = current.strftime("%I:%M %p")
    d2 = today.strftime("%B %d, %Y")

#------------------------------------------------
    city_weather = {
        'city': city,
        'temperature': celsius,
        'description': r['weather'][0]['description'],
        'id': r['weather'][0]['id'],
        'Humidity': (r['main']['humidity']),
        'wind': r['wind']['speed'],
        'lon':r['coord']['lon'],
        'lat':r['coord']['lat'],
        'Date':d2,
        'time':time
    }
    print(city_weather)
    lon=city_weather['lon']
    lat=city_weather['lat']
    context = {'city_weather': city_weather}
    return render(request,'page2.html', context)





