class Fruit:
    def taste(self):
        print("Fruit has a taste")


class Orange(Fruit):
    def taste(self):
        print("Orange is sour and sweet")


org = Orange()
org.taste()
