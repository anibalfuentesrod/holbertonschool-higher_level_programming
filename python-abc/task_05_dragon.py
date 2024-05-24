"""
Making a mixing class!!!
"""


class SwimMixin:
    """
    A mixing class providing swim functionality
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class providing fly functuonality
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class respresenting a DRAGON, inheriting, Swim... and Fly....
    """
    def roar(self):
        print("The dragon roars!")

    def fire(self):
        print("The dragon shoots fire!")
