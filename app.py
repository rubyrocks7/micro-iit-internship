import requests
api_key = '9b6546c76a3d17643ccb2160724b9060'
user_input = input("Enter City:")
weather_data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+user_input+'&appid='+api_key).json()
if weather_data.json()['cod'] == '404':
    print("City not found")
    exit()
else :      
    weather = weather_data.json()['weather'][0]['description']
    temp   = weather_data.json()['main']['temp']
    print(f"The weather in {user_input} is {weather} and the temperature is {temp}K")


