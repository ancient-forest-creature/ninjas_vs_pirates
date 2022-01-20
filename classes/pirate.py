import random

class Pirate:

    pirate_name = ""

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 1000
        Pirate.pirate_name = name

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength * random.ranint(1,12)
        return self

