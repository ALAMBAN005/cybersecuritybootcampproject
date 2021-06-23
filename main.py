import requests

from datetime import datetime

user_api = '8a463c46a58c2455b3dbe17ed9daabb6'
location = input("Enter the name of city: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api


api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

temp = ((api_data['main'] ['temp']) - 273.15) 
weather_desc = api_data['weather']['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime(" %d %b %Y" | "&I:%M:%S %p")
                    
                    
print("X------------------------------------------------------------------")
print("Weather Statistics For {} || {}".format(location.upper(), date_time))
print("X------------------------------------------------------------------")


print("Current Temperature : {.2f} deg C".format(temp))
print("Current Weather Description :",weather_desc)
print("Current Humidity :",hmdt, '%')
print("Current Wind Speed :",wind_spd, 'kmph')
print("The above details are successfully stored in the text file.")
    
with open('Weather report.txt','w')as f:
  f.write(temp)
  f.write(weather_desc)
  f.write(hmdt)
  f.write(wind_spd)