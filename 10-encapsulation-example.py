class OrangeBasket:
    def __init__(self, count):
        self.__count = count

    def add(self, amount):
        self.__count += amount

    def get_count(self):
        return self.__count


basket = OrangeBasket(10)
basket.add(5)
print(basket.get_count())
