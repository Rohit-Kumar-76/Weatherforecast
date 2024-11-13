import requests
from django.shortcuts import render

def weather(request):
    city = request.GET.get('city', 'New York')  # Default city
    api_key = '7b409572a085400bd7bfa1cd929c4250'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json() if response.status_code == 200 else None
    
    context = {
        'data': data,
        'city': city,
    }
    return render(request, 'forecast/weather.html', context)
