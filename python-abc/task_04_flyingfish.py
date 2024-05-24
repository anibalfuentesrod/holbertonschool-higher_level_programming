"""
Creating multiple classes that inherits
"""


class Fish:
    """
    ......A class representing a fish
    """
    def swim(self):
        print("The fish is swimming")

    def habitad(self):
        print("The fish lives in water")


class Bird:
    """
    Class that represents a bird duhh
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    This class represents a flying fish, inherited both Fish and Bird
    """
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and in the sky!")
