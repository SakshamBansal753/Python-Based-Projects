print("Welcome To Adventure Game ")
import random
print(r"""
              _                 _                     _____                      
     /\      | |               | |                   / ____|                     
    /  \   __| __   _____ _ __ | |_ _   _ _ __ ___  | |  __  __ _ _ __ ___   ___ 
   / /\ \ / _` \ \ / / _ | '_ \| __| | | | '__/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \
  / ____ | (_| |\ V |  __| | | | |_| |_| | | |  __/ | |__| | (_| | | | | | |  __/
 /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|  \_____|\__,_|_| |_| |_|\___|
                                                                                 
                                                                                 
     """)
easy_villans=["Zombie","Vampire","Wolfman"]
medium_villans=["Dracula","MagmaGolem","Lava_rock"]
hard_villans=["Witch","Thanos","Demon"]
def easy_fight(hp):
    fight_villian=random.choice(easy_villans)
    hp_villian=1200

    if fight_villian=="Zombie":
         print("Your Opponent is Zombie")
         print(f"Villain hp is {hp_villian}")
         print(f"Your Hp is {hp}")
         while hp>0 and hp_villian>0:
           villain_attack=["brain eater","Memory Eater","blood bath","Rage"]
           random_attack=random.choice(villain_attack)
           
           user_attack=["1)Blood rise","2)Riffle Assault","3)Holy cross throw","4)Grenade burst"]
           print("Your Attacks are:")
           for string in user_attack:
               print(f"{string}")
           choose_attack=int(input("Type number for your attack"))
           if choose_attack==1:
               hp_villian-=200
               print(f"villain Hp is {hp_villian}")
           elif choose_attack==2:
               hp_villian-=150
               print(f"villain Hp is {hp_villian}")
           elif choose_attack==3:
               hp_villian-=210
               print(f"villainHp is {hp_villian}")
           elif choose_attack==4:
               hp_villian-=200
               print(f"villain Hp is {hp_villian}")
           else:
               print("Invalid ")
               
           if random_attack=="Memory eater":
               hp-=200
               print(f"User is  Attacked by {random_attack}")
               print(f"Your Hp is {hp}")
           if random_attack=="brain eater":
               hp-=200
               print(f"User is  Attacked by {random_attack}")

               print(f"Your Hp is {hp}")
           if random_attack=="blood bath":
               hp-=250
               print(f"User is  Attacked by {random_attack}")
               print(f"Your Hp is {hp}")
           if random_attack=="Rage":
               hp-=200
               print(f"User is  Attacked by {random_attack}")
               print(f"Your Hp is {hp}")
           if hp_villian<=300:
               hp_villian-=100
               print("A special attack energy drain in villain about 100 points")
    if fight_villian == "Vampire":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Blooddrain", "redbite", "Bloody moonfall", "Delusion"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Blooddrain":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "redbite":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Bloody moonfall":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Delusion":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300:
                hp_villian -= 100
                print("A special attack energy drain in villain about 100 points")
    if fight_villian == "Wolfman":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Blood bite", "Howling crash", "Fury Swipe", "Howling bite"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Blood bite":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Howling crash":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Howling bite":
                hp -= 200

                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Fury Swipe":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300:
                hp_villian -= 100
                print("A special attack energy drain in villain about 100 points")

    if hp!=0:
        return True
    else:
        return False


def medium_fight(hp):
    fight_villian = random.choice(medium_villans)
    hp_villian = 1400

    if fight_villian == "Dracula":
        print(f"Your Opponent is {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["bat swarm", "Dracula bite", "Dark Magic Blast", "Shadow Teleport"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 170
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "bat swarm":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Dracula bite":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")

                print(f"Your Hp is {hp}")
            if random_attack == "Dark Magic Blast":
                hp -= 250
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Shadow Teleport ":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count==0:
                hp_villian -=100
                count+=1
                print("A special attack energy drain in villain about 100 points")
    if fight_villian == "MagmaGolem":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Titan Punch", "Molten Rock Throw", "Eruption Wave", "Heat Pulse"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Titan Punch":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Molten Rock Throw":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Eruption Wave":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Heat Pulse":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count == 0:
                hp_villian -= 100
                count += 1
                print("A special attack energy drain in villain about 100 points")
    if fight_villian == "Lava_rock":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Sesmic Smash", "Lava Boulder Toss", "Flame Surge", "Magma Spikes"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Sesmic Smash":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Lava Boulder Toss":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Magma Spikes":
                hp -= 200

                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Flame Surge":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count == 0:
                hp_villian -= 100
                count += 1
                print("A special attack energy drain in villain about 100 points")

    if hp != 0:
        return True
    else:
        return False

def hard_fight(hp):
    fight_villian = random.choice(hard_villans)
    hp_villian = 1600
    hp+=200

    if fight_villian == "Witch":
        print(f"Your Opponent is {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Hex Bolt", "Cursed Flames", "Dark Magic Blast", "Dark Explosion"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 170
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Hex Bolt":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Cursed Flames":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")

                print(f"Your Hp is {hp}")
            if random_attack == "Dark Magic Blast":
                hp -= 250
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Dark Explosion ":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count==0:
                hp_villian -=100
                count+=1
                print("A special attack energy drain in villain about 100 points")
    if fight_villian == "Thanos":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Titan Punch", "Power Stone Blast", "Reality Warp", "Ground Shockwave"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Titan Punch":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Power Stone Blast":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Reality Warp":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Ground Shockwave":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count == 0:
                hp_villian -= 100
                count += 1
                print("A special attack energy drain in villain about 100 points")
    if fight_villian == "Lava_rock":
        print(f"Your Opponent {fight_villian}")
        print(f"Villain hp is {hp_villian}")
        print(f"Your Hp is {hp}")
        count=0
        while hp > 0 and hp_villian > 0:
            villain_attack = ["Sesmic Smash", "Lava Boulder Toss", "Flame Surge", "Magma Spikes"]
            random_attack = random.choice(villain_attack)

            user_attack = ["1)Blood rise", "2)Riffle Assault", "3)Holy cross throw", "4)Grenade burst"]
            print("Your Attacks are:\n")
            for string in user_attack:
                print(f"{string}")
            choose_attack = int(input("Type number for your attack"))
            if choose_attack == 1:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 2:
                hp_villian -= 150
                print(f"villain Hp is {hp_villian}")
            elif choose_attack == 3:
                hp_villian -= 210
                print(f"villainHp is {hp_villian}")
            elif choose_attack == 4:
                hp_villian -= 200
                print(f"villain Hp is {hp_villian}")
            else:
                print("Invalid ")

            if random_attack == "Sesmic Smash":
                hp -= 220
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Lava Boulder Toss":
                hp -= 200
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Magma Spikes":
                hp -= 200

                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if random_attack == "Flame Surge":
                hp -= 150
                print(f"User is  Attacked by {random_attack}")
                print(f"Your Hp is {hp}")
            if hp_villian <= 300 and count == 0:
                hp_villian -= 100
                count += 1
                print("A special attack energy drain in villain about 100 points")

    if hp != 0:

        return True
    else:
        return False
is_continue=True
while is_continue:
    game_level=input("Which level of difficulty you want\n Easy\n Medium \n Hard\n Each level represent by first letter").lower()
    hp_player = 1000

    if game_level=="e":

        print(r"""
                    ╔════════════════════════╗
                    ║      ⚔ BATTLE ⚔        ║
                    ╠════════════════════════╣
                    ║      Fight Begins!     ║
                    ╚════════════════════════╝

                    """)
        is_win=easy_fight(hp_player)
    elif game_level=="m":
        print(r"""
                    ╔════════════════════════╗
                    ║      ⚔ BATTLE ⚔        ║
                    ╠════════════════════════╣
                    ║      Fight Begins!     ║
                    ╚════════════════════════╝

                    """)
        is_win=medium_fight(hp_player)
    elif game_level=="h":
        print(r"""
                    ╔════════════════════════╗
                    ║      ⚔ BATTLE ⚔        ║
                    ╠════════════════════════╣
                    ║      Fight Begins!     ║
                    ╚════════════════════════╝

                    """)
        is_win=hard_fight(hp_player)
    else:
        print("Invalid")
    if is_win:
        print("\nYou defeated the villain!")
        continue_not=input("Do you Want To Continue if yes type y or no for n").lower()
        if continue_not=="n":
            is_continue=False
        elif continue_not=="y":
            is_continue=True
        else:
            print("Invalid")
    else:
        print("\nYou Lost by the villain!")
        continue_not = input("Do you Want To Continue if yes type y or no for n").lower()
        if continue_not == "n":
            is_continue = False

        elif continue_not == "y":
            is_continue = True
            print("\nYou defeated the villain!")
        else:
            print("Invalid")
