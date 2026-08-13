from abc import ABC, abstractmethod


# Abstraction
class Food(ABC):
    @abstractmethod
    def color(self):
        pass


# Inheritance
class Fruit(Food):
    def type(self):
        print("Type of food is fruit")


# Encapsulation
class Citrus(Fruit):
    __taste = "sour"

    def taste(self):
        return self.__taste


# Polymorphism
class Lemon(Citrus):
    def color(self):
        print("Color of lemon is green")


class Orange(Citrus):
    def color(self):
        print("Color of orange is orange")


for fruit in (Lemon(), Orange()):
    fruit.color()
