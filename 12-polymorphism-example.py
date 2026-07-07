class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


for animal in (Cat(), Cow()):
    animal.sound()
