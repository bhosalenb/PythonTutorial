
from enum import Enum
class A:
    pass

class countries(Enum):
    INDIA = 1
    UK = 2
    USA = 3

#print(countries.INDIA)
#print(countries(1))
print(A)
print(countries)

for country in countries:
    print(country,country.value)
