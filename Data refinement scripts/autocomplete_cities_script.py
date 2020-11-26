#Don't run, this has done its work
import csv

countries = []
with open("major_countries.txt",'r') as file:
    for line in file:
        country = line.lower()
        if(country[-1] == '\n'):
            country = country[0:-1]
        countries.append(country)

major_countries = []

with open("major_cities_original.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    firstRow = True
    cityTuple = ("first_nothing_no_city",)
    for row in reader:
        if(firstRow == True):
            firstRow = False
        else:
            currCountry = row[1].lower()
            if(currCountry not in countries):
                continue
            elif currCountry not in major_countries:
                major_countries.append(currCountry)



regular_alphabet = "abcdefghijklmnopqrstuvwxyz -"
cities = []


with open("major_cities_original.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    firstRow = True
    cityTuple = ("first_nothing_no_city",)
    for row in reader:
        if(firstRow == True):
            firstRow = False
        else:
            currCountry = row[1].lower()
            if(currCountry in major_countries):
                cityTuple = (row[0].lower(),)
                should_not_add = False
                for char in cityTuple[0]:
                    if(char not in regular_alphabet):
                        should_not_add = True
                        break
                if(should_not_add == True or cityTuple in cities):
                    continue
                cities.append(cityTuple)


with open("autocomplete_cities.csv",'w',newline = '',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(("cities",))
    writer.writerows(cities)

print(1)
            