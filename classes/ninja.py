import random

class Ninja:

    ninja_name = ""

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 500
        self.hidden = True
        self.special = 3
        self.victory = f"The battlefield is silent as pirate blood soaks the ground.\n {name} stands victorious over their enemies."
        Ninja.ninja_name = name
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength * random.randint(1,10)
        return self

    def surprise_attack(self, pirate):
        pirate.health -= self.strength * random.randint(5,15)
        return self
    
    def disappear(self):
        result =  self.speed * random.randint(1,10) // 15
        if result >= 1:
            self.hidden = True
            print("The Ninjas disappear in a puff of smoke! They are no where to be seen.")
        else:
            self.hidden = False
            print("The ninjas try to hide but have failed.")

    @staticmethod
    def set_attack(speed):
        return speed * random.randint(2,6) // 10