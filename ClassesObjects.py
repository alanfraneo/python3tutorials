
class Fish:
    size = "large"
    color = "white"

    def swim(self):
        print("the", self.size, self.color, "fish is swimming")


goldfish = Fish()
goldfish.swim()
goldfish.size = "small"
goldfish.color = "gold"
goldfish.swim()


class MarineCreatures:
    """ class variables and instance variables differentiated in this example"""

    size = "large"  # class variable, available to all objects of this class

    def __init__(self, color):
        self.color = color  # instance variable, which can be called during object creation

    def swim(self):
        print("A", self.size, self.color, "marine creature is swimming")

# seahorse = MarineCreatures()  # this wouldn't work, will throw an error
seahorse = MarineCreatures("blue")
seahorse.swim()
