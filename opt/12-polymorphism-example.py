class Lemon:
    def taste(self):
        print("Lemon is sour")


class Orange:
    def taste(self):
        print("Orange is sweet")


for fruit in (Lemon(), Orange()):
    fruit.taste()
