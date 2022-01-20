from classes.ninja import Ninja
from classes.pirate import Pirate
import random

rand_var = 0
while rand_var < 1:
    # print(rand_var)
    rand_var += 1
    select = input("[N]inija or [P]irate?")
    # print(select)

    if select == "N" or select == "n":
        player = Ninja("Wispered Death")
        rand_var = 1
    elif select == "P" or select == "p":
        player = Pirate("The Jolly Rodgers")
        rand_var = 1
    else:
        print("Invalid selection. Please selct N for Ninja or P for Pirate.\n")
        rand_var = 0

# player.show_stats()

print(player.set_attack(player.speed))