import requests, json
import API_KEY
import sql_connector as sqlman #codename for sql-yuvraj

sqlObj = sqlman.simple_sql()

class Weather:
    def __init__(self,temperatureIN,humidityIN):
        self.temp = temperatureIN
        self.humidity = humidityIN
    
def getWeatherAtPlace(place_name):

    place_name_LC = place_name.lower()
    url = "http://api.openweathermap.org/data/2.5/weather?"

    url = url + "appid=" + API_KEY.openweathermap2 +  "&q=" + place_name_LC
    print(url) #prototyping fricker, get quikrr
    response = requests.get(url)
    allINFO = response.json()

    if(place_name_LC != ""):
        sqlObj.addToSearches(place_name_LC)

    if (allINFO["cod"]  == "404") or (allINFO["cod"] =='400'):
        print("ERROR PLACE DOES NOT EXIST")
        return ("!Not a Real Place")
    else:
     #   try:
      #      sqlObj.addToSaved(place_name_LC)
       # except:
        #    print("You fool!, you thought I would not see this coming?")
            #instead of doing nothing, it will now create the place in the database if it exists with the weather api
         #   sqlObj.addToPlaces(place_name_LC)
          #  sqlObj.addToSaved(place_name_LC)
        weatherINFO = allINFO['main']
        #sysINFO = allINFO['sys'] #info here for future expandability
        weatherOBJ = (str(round(weatherINFO["temp"]-273.15))+"°C",str(weatherINFO["humidity"])+"% Humidity")
        #fixed error dict referencing error
        #print(weatherINFO)
        return weatherOBJ

def loadSavedPlaces():
    return sqlObj.getLastSaved()

def checkIfActualPlace(place_name):
    if(place_name == ''):
        return False
    place_name_LC = place_name.lower()
    url = "http://api.openweathermap.org/data/2.5/weather?"

    url = url + "appid=" + API_KEY.openweathermap2 +  "&q=" + place_name_LC

    response = requests.get(url)
    info = response.json()

    if(info["cod"] == "404" or info["cod"] == '400'):
        return False
    return True