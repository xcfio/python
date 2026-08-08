from abc import ABC, abstractmethod


class Fruit(ABC):
    @abstractmethod
    def taste(self):
        pass


class Orange(Fruit):
    def __init__(self, size):
        self.size = size

    def taste(self):
        return self.size * self.size


o = Orange(4)
print(o.taste())
