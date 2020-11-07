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
    print(url)
    response = requests.get(url)

    allINFO = response.json()
    

    if (allINFO["cod"]  != "404"):
        weatherINFO = allINFO['main']
        #sysINFO = allINFO['sys'] #info here for future expandability
        weatherOBJ = (str(round(weatherINFO["temp"]-273.16))+"°C",str(weatherINFO["humidity"])+"% Humidity")
    #fixed error dict referencing error 
        #print(weatherINFO)
        return weatherOBJ
    else:
        print("ERROR PLACE DOES NOT EXIST")
        return "Not a Real Place"