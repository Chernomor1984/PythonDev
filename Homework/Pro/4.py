"""
Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном порядке список 
primary городов с населением более 10000000 человек, в формате:

Cities: Beijing, Buenos Aires, ...
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]
"""
from functools import reduce

data = [
    ['Tokyo', 35_676_000, 'primary'],
    ['New York', 19_354_922, 'nan'],
    ['Mexico City', 19028000, 'primary'],
    ['Mumbai', 18978000, 'admin'],
    ['Sao Paulo', 18845000, 'admin'],
    ['Delhi', 15926000, 'admin'],
    ['Shanghai', 14987000, 'admin'],
    ['Kolkata', 14787000, 'admin'],
    ['Los Angeles', 12815475, 'nan'],
    ['Dhaka', 12797394, 'primary'],
    ['Buenos Aires', 12795000, 'primary'],
    ['Karachi', 12130000, 'admin'],
    ['Cairo', 11893000, 'primary'],
    ['Rio de Janeiro', 11748000, 'admin'],
    ['Osaka', 11294000, 'admin'],
    ['Beijing', 11106000, 'primary'],
    ['Manila', 11100000, 'primary'],
    ['Moscow', 10452000, 'primary'],
    ['Istanbul', 10061000, 'admin'],
    ['Paris', 9904000, 'primary']
]

primaryCityItems = filter(lambda item: item[2] == "primary" and item[1] > 10_000_000, data)
primaryCities = sorted(map(lambda item: item[0], primaryCityItems))
initialStringValue = "Cities: "
citiesString = reduce(lambda initial, city: initial + ("" if initial == initialStringValue else ", ") + city, primaryCities, initialStringValue)
print(citiesString)