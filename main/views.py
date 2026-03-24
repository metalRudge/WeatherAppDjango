import requests
from django.shortcuts import render
from .models import SearchHistory

API_KEY = "4246f9c69acc6507f2cb6cf19f556ec0"

def index(request):
    weather = None
    error = None
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]


    if request.method == "POST":
        city = request.POST.get('city', '').strip()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                resp = requests.get(url,timeout=5)
                data = resp.json()

                if(resp.status_code == 200):
                    weather = {
                        'city': f"{data['name']},{data['sys']['country']}",
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'description': data['weather'][0]['description'].title(),
                        'icon': data['weather'][0]['icon'],
                    }
                    # save to database
                    SearchHistory.objects.create(
                        city_name = data['name'],
                        temperature = data['main']['temp'],
                        humidity = data['main']['humidity'],
                        pressure = data['main']['pressure'],
                        description = data['weather'][0]['description'].title()
                    )
                    #refresh recent searches
                    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
                else:
                    error = data.get("message","Couldn't load Weather Data")
            except requests.RequestException:
                error = "Network error. Please try again"
        else:
            error = "Unexpected error.Please enter a valid city name."
    return render(request,"main/index.html",{'weather':weather,'error': error,'recent_searches': recent_searches})
