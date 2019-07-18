import requests

API_key = "01023234a094fcbf44c36d03fae899a8"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name : ")

Final_url = base_url + "appid=" + API_key + "&q=" + city_name
weather_data = requests.get(Final_url).json()

# JSON data works just similar to python dictionary and you can access the value using [].
# Accessing Temperature, temperature resides in main and its key is temp
temp = weather_data['main']['temp']

# Accessing wind speed, it resides in wind and its key is speed
wind_speed = weather_data['wind']['speed']

# Accessing Description, it resides in weather and its key is description
description = weather_data['weather'][0]['description']

# Accessing Latitude, it resides in coord and its key is lat
latitude = weather_data['coord']['lat']

# Accessing Longitude, it resides in coord and its key is lon
longitude = weather_data['coord']['lon']

# Printing Data
print('\nTemperature : ', temp)
print('\nWind Speed : ', wind_speed)
print('\nDescription : ', description)
print('\nLatitude : ', latitude)
print('\nLongitude : ', longitude)