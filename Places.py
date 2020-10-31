import Weather

class Places:
    #also store a database here
    def __init__(self,db):
        self.db = db
        self.places = []
    
    def addPlace(self,place_name):
        self.places.append(place_name)
        #self.db.add(place_name)
    
    def removePlace(self, place_name):
        if(place_name not in self.places):
            print("PLACE BEING REMOVED IS NOT PART OF DATABASE")
            return
        self.places.remove(place_name)
        #self.db.remove(place_name)
    
    def loadPlaces(self,db):
        #load places from database
        print(1)

    def getWeather(self, API_KEY):
        weatherList = []
        for place in self.places:
            weatherList.append(Weather.getWeatherAtPlace(place,API_KEY))

