import requests, json
import API_KEY

class Weather:
    def __init__(self,temperatureIN,humidityIN):
        self.temp = temperatureIN
        self.humidity = humidityIN
    

def getWeatherAtPlace(place_name):
    place_name_LC = place_name.lower()
    url = "http://api.openweathermap.org/data/2.5/weather?"

    url = url + "appid=" + API_KEY.openweathermap2 +  "&q=" + place_name_LC
    
    response = requests.get(url)

    weatherINFO = response.json()
    
    if(weatherINFO["cod"]  == 404):
        print("ERROR PLACE DOES NOT EXIST")
        return    
    #shows error on line 24 trying to fix
    weatherOBJ = Weather(weatherINFO["temp"],weatherINFO["humidity"])

    return weatherOBJ

