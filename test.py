import Weather

place=str(input('Enter city name:  '))
place_lc=place.lower()

x=Weather.getWeatherAtPlace(place_lc)
print(x)
