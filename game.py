# from tkinter.tix import Tree
from classes.ninja import Ninja
from classes.pirate import Pirate
import random

round = 0
proper_select = 0
while proper_select < 1:
    select = input("[N]inija or [P]irate?")

    if select == "N" or select == "n":
        player = Ninja("Wispering Death")
        opponent = Pirate("The Jolly Rodgers")
        proper_select = 1
    elif select == "P" or select == "p":
        player = Pirate("The Dreadnoghts")
        opponent = Ninja("Black Sun")
        proper_select = 1
    else:
        print("Invalid selection.\nPlease selct N for Ninja or P for Pirate.\n")
        proper_select = 0

print(f"A foul wind blows. \nThe sun turns to dusk. \nThe dreaded pirates known as the {Pirate.pirate_name} can feel something is amiss")
print(f"The air is thick with smoke and noise. \nThe gulls circle and bank. \n")
print(f"This land is guarded by the {Ninja.ninja_name}, and they do not take kindly to intrusions by smelly pirates.")
print("The for battle is here! Fight! fight for your lives!")

is_dead = False
if select == "N" or select == "n":
    print("\nNinja Stats:")
    player.show_stats()
    print("\nPirate Stats:")
    opponent.show_stats()
    print("Ninjas have the element of surprise. Their special Suprise Attack is ready!")
    while is_dead == False:
        num_attacks = player.set_attack(player.speed)
        print(f"number of attacks is: {num_attacks}")
        for i in range(num_attacks):
            round_select = 0
            while round_select < 1:
                if (player.hidden == True):
                    print("Ninjas appear from nowhere and attack!")
                    player.surprise_attack(opponent)
                    opponent.show_stats()
                    player.hidden = False
                    player.special = 1
                    if opponent.health <= 0:
                        is_dead = True
                    round_select = 1
                elif (player.special > 2):
                    action = input("You can [A]ttack or try to [D]issapear for your special attack. \nWhat do you do?")
                    if action == "A" or action == "a":
                        player.attack(opponent)
                        opponent.show_stats()
                        player.hidden = False
                        player.special = player.special + 1
                        if opponent.health <= 0:
                            is_dead = True
                        round_select = 1
                    elif action == "D" or action == "d":
                        player.disappear()
                        round_select = 1
                    else:
                        print("Invalid selection. Please try again")

# print(f"select is: {select}")
# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

print ("\nOUT\n")

player.show_stats()

attk = random.randint(1, 10)
print(attk)