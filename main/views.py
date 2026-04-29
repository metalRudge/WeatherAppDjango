import requests
from .services.station_reader import load_stations_data
from django.shortcuts import render,redirect,get_object_or_404
from .models import SearchHistory,WeatherStation
from decouple import config
API_KEY = config('OPENWEATHER_API_KEY')


def index(request):
    weather = None
    error = None
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
    stations_data, stations_error = load_stations_data()
    active_tab = request.GET.get('tab','dashboard')
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_station':
            id = request.POST.get('station_id', '').strip()
            name = request.POST.get('station_name', '').strip()
            loc = request.POST.get('station_loc', '').strip()
            if not id:
                error = "ID field cannot be empty - ID required."
            elif not WeatherStation.objects.filter(station_id=id).exists():
                WeatherStation.objects.create(station_id=id, station_name=name, station_loc=loc)
                return redirect('/?' + 'tab=dashboard')
            else:
                error = "A station with the same ID already exists."

        elif action == 'delete_station':
            station_id = request.POST.get('station_id')
            station = get_object_or_404(WeatherStation, id=station_id)
            station.delete()
            return redirect('/?' + 'tab=dashboard')
        
        stations_data, stations_error = load_stations_data()

    return render(request,"main/index.html",{'error': error,"active_tab": active_tab,'stations':WeatherStation.objects.all(),'stations_data':stations_data,'stations_error':stations_error,},)

