import requests


api_key = '7b76170c241d586d039d5d05537de265'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("City not found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"Weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}F")


