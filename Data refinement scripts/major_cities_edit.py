#do not put this in the final proj, just here to show what I changed in major_cities.csv

#you do not need to run this, it has done its work

import csv

regular_alphabet = "abcdefghijklmnopqrstuvwxyz -"

cities = []
with open("major_cities.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    firstRow = True
    cityTuple = ("first_nothing_no_city",)
    for row in reader:
        if(firstRow == True):
            firstRow = False
        else:
            cityTuple = (row[0].lower(),)
            should_not_add = False
            for char in cityTuple[0]:
                if(char not in regular_alphabet):
                    should_not_add = True
                    break
            if(should_not_add == True or cityTuple in cities):
                continue
            cities.append(cityTuple)

with open("major_cities.csv",'w',newline = '',encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(("cities",))
    writer.writerows(cities)