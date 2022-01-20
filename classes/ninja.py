import random

class Ninja:

    ninja_name = ""

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 1000
        self.hidden = True
        self.special = 3
        # self.disappear = False
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
        result = self.speed * random.randint(1,10) // 25
        if result > 1:
            self.hidden = True
            print("The Ninjas disappear in a puff of smoke! They are no where to be seen.")
        else:
            self.hidden = False
            print("The ninjas try to hid but have failed.")

    @staticmethod
    def set_attack(speed):
        # base = speed * random.randint(2,6)
        # print(base)
        # print("1st:")
        # print( base // 10 )
        return speed * random.randint(2,6) // 10