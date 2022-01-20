import random

class Pirate:

    pirate_name = ""

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 500
        self.special = 1
        self.loaded = False
        Pirate.pirate_name = name

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength * random.randint(1,10)
        return self

    def volly(self, ninja):
        ninja.health -= self.strength * random.randint(4,13)
        return self

    def broadside(self, ninja):
        ninja.health -= self.strength * random.randint(8,20)
        return self
    
    @staticmethod
    def set_attack(speed):
        return speed * random.randint(3,6) // 9