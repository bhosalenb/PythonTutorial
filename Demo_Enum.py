from enum import Enum

class countries(Enum):
    INDIA = 1
    UK = 2
    USA = 3

#print(countries.INDIA)
#print(countries(1))

for country in countries:
    print(country)
