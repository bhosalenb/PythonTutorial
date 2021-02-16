from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        None

class Tiger(Animal):
    def eat(self):
        print("This animal is Non vegetarian")

class Goat(Animal):
    def eat(self):
        print("This animal is vegetarian")

a = ABC()
#a.eat()
t = Tiger()
t.eat()

g = Goat()
g.eat()