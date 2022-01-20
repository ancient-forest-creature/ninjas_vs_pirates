import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def rounds_n(player, opponent):
    while player.health > 0 or opponent.health > 0:
        num_attacks = player.set_attack(player.speed)
        print(f"{player.name} get {num_attacks} attacks")
        for i in range(num_attacks):
            round_select = 0
            while round_select < 1:
                if (player.hidden == True):
                    action = input("The ninjas are poised and waiting in the shadows to attack!\nHit Enter to attack!")
                    print("Ninjas appear from nowhere and attack!")
                    player.surprise_attack(opponent)
                    opponent.show_stats()
                    player.hidden = False
                    player.special = 1
                    if opponent.health <= 0:
                        return
                    round_select = 1
                elif (player.special > 2):
                    action = input("You can [A]ttack or try to [D]issapear for your special attack. \nWhat do you do?")
                    if action == "A" or action == "a":
                        player.attack(opponent)
                        opponent.show_stats()
                        player.hidden = False
                        player.special = player.special + 1
                        if opponent.health <= 0:
                            return
                        round_select = 1
                    elif action == "D" or action == "d":
                        player.disappear()
                        round_select = 1
                    else:
                        print("Invalid selection. Please try again")
                else:
                    action = input("The battel rages and ninjas continue to fight!\nHit Enter to attack!")
                    player.attack(opponent)
                    opponent.show_stats()
                    player.hidden = False
                    player.special = player.special + 1
                    if opponent.health <= 0:
                        return
                    round_select = 1
        num_attacks_opp = opponent.set_attack(opponent.speed)
        print(f"{opponent.name} get {num_attacks_opp} attacks")
        for i in range(num_attacks_opp):
            round_select = 0
            while round_select < 1:
                if (player.hidden == True):
                    print("The pirates are ready for the fight, but the ninjas are no where in sight.")
                    round_select = 1
                elif (player.special > 3):
                    print("The pirates have the cannons loaded and ready for a broadside!\n")
                    print("Cannon roar firing shot, chain, and death!")
                    opponent.broadside(player)
                    player.show_stats()
                    opponent.special = 1
                    if player.health <= 0:
                        return 
                    round_select = 1
                elif (opponent.loaded == True):
                    print("The pirates muskets are loaded! They fire a volly!")
                    opponent.volly(player)
                    player.show_stats()
                    opponent.loaded = False
                    opponent.special = opponent.special + 1
                    if player.health <= 0:
                        return
                    round_select = 1
                else:
                    if player.health <= 250:
                        print("The pirates load thier muskets for a volloy!")
                        opponent.loaded = True
                        opponent.special = opponent.special + 1
                        round_select = 1
                    else:
                        print("The pirates attack!")
                        opponent.attack(player)
                        player.show_stats()
                        opponent.special = opponent.special + 1
                        if player.health <= 0:
                            return
                        round_select = 1

def rounds_p(player, opponent):
    while player.health > 0 or opponent.health > 0:
        num_attacks_opp = opponent.set_attack(opponent.speed)
        print(f"number of Ninja attacks is: {num_attacks_opp}")
        for i in range(num_attacks_opp):
            round_select = 0
            while round_select < 1:
                if (opponent.hidden == True):
                    print("Ninjas appear from nowhere and attack!")
                    opponent.surprise_attack(player)
                    player.show_stats()
                    opponent.hidden = False
                    opponent.special = 1
                    if player.health <= 0:
                        return
                    round_select = 1
                elif (opponent.special > 2):
                    if i < 2:
                        opponent.disappear()
                        round_select = 1
                    else:
                        ("The ninjas continue to attack!")
                        opponent.attack(player)
                        player.show_stats()
                        opponent.hidden = False
                        opponent.special = opponent.special + 1
                        if player.health <= 0:
                            return
                        round_select = 1
                else:
                    print("The battel rages and ninjas continue to fight!\n")
                    opponent.attack(player)
                    player.show_stats()
                    opponent.hidden = False
                    opponent.special = opponent.special + 1
                    if player.health <= 0:
                        return
                    round_select = 1
        num_attacks = player.set_attack(player.speed)
        print(f"number of pirate attacks is {num_attacks}")
        for i in range(num_attacks):
            round_select = 0
            while round_select < 1:
                if (opponent.hidden == True):
                    print("The pirates are ready for the fight, but the ninjas are no where in sight.")
                    round_select = 1
                elif (player.special > 4):
                    action = input("The pirates have the cannons loaded and ready for a broadside!\nHit Enter to attack!")
                    print("Cannon roar firing shot, chain, and death!")
                    player.broadside(opponent)
                    opponent.show_stats()
                    player.special = 1
                    if opponent.health <= 0:
                        return 
                    round_select = 1
                elif (player.loaded == True):
                    action = input("You can [A]ttack or [V]olly!\nWhich do you choose?")
                    player.attack(opponent)
                    opponent.show_stats()
                    player.special = player.special + 1
                    if opponent.health <= 0:
                        return
                    round_select = 1
                else:
                    action = input("You can [A]ttack or [L]oad for a volly. \nWhat do you do?")
                    if action == "A" or action == "a":
                        player.attack(opponent)
                        opponent.show_stats()
                        player.special = player.special + 1
                        if opponent.health <= 0:
                            return
                        round_select = 1
                    elif action == "L" or action == "l":
                        player.loaded = True
                        round_select = 1
                    else:
                        print("Invalid selection. Please try again")

    