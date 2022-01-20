from classes.ninja import Ninja
from classes.pirate import Pirate
import mechanics

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

mechanics.cls()
print(f"A foul wind blows. \nThe sun turns to dusk. \nThe dreaded pirates known as the {Pirate.pirate_name} can feel something is amiss")
print(f"The air is thick with smoke and noise. \nThe gulls circle and bank. \n")
hold = input("\nHit Enter to continue \n")
mechanics.cls()
print(f"This land is guarded by the {Ninja.ninja_name}, and they do not take kindly to intrusions by smelly pirates.")
print("The for battle is here! Fight! fight for your lives!")
hold = input("\nHit Enter to continue \n")
mechanics.cls()

# mechanics.is_dead = False
print("\nNinja Stats:")
player.show_stats()
print("\nPirate Stats:")
opponent.show_stats()
if select == "N" or select == "n":
    print("Ninjas have the element of surprise. Their special Suprise Attack is ready!")
    mechanics.rounds_n(player, opponent)
else:
    mechanics.rounds_p(player, opponent)

# print(f"select is: {select}")
# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

print ("\nOUT\n")