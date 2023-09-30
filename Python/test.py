from datetime import datetime

weather_data = {'coord': {'lon': -117.1286, 'lat': 33.5217},
             'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
             'base': 'stations',
             'main': {'temp': 60.53, 'feels_like': 60.19, 'temp_min': 58.21, 'temp_max': 63.09, 'pressure': 1012, 'humidity': 83}, 
             'visibility': 10000,
             'wind': {'speed': 4, 'deg': 229, 'gust': 5.99},
             'clouds': {'all': 100},
             'dt': 1696086130,
             'sys': {'type': 2, 'id': 2080907, 'country': 'US', 'sunrise': 1696081315, 'sunset': 1696124102},
             'timezone': -25200,
             'id': 0,
             'name': 'Temecula',
             'cod': 200}


def print_weather_data(weather_data):
    hpa_to_mmHg_conversion_factor = 33.86389
    pressure_mmHg = str(round(float(weather_data['main']['pressure'])/hpa_to_mmHg_conversion_factor,2))
    utc_sunrise_time = (weather_data['sys']['sunrise'] + weather_data['timezone'])
    utc_sunset_time = (weather_data['sys']['sunset'] + weather_data['timezone'])

    print(F"Location (City, Country): {weather_data['name']}, {weather_data['sys']['country']}")
    print(F"Geo coordinates (Lon , Lat): {weather_data['coord']['lon']}, {weather_data['coord']['lat']}")
    print(F"Current temperature: {weather_data['main']['temp']}")
    print(F"Feels like: {weather_data['main']['feels_like']}")
    print(F"Humidity (%): {weather_data['main']['humidity']}")
    print(F"Max temperature: {weather_data['main']['temp_max']}")
    print(F"Min temperature: {weather_data['main']['temp_min']}")
    print(F"Air Pressure (mm Hg): {pressure_mmHg}")
    print(F"Weather description: {weather_data['weather'][0]['description']}")
    print(F"Weather condition: {weather_data['weather'][0]['main']}")
    print("Sunrise:", datetime.utcfromtimestamp(utc_sunrise_time).strftime('%Y-%m-%d %H:%M:%S'))
    print("Sunset:" , datetime.utcfromtimestamp(utc_sunset_time).strftime('%Y-%m-%d %H:%M:%S'))


print_weather_data(weather_data)