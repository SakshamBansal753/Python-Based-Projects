print("Welcome To Adventure Game ")
import random
from data import easy_villans
from data import user_attacks
from data import medium_villains
from data import hard_villans
print(r"""
              _                 _                     _____                      
     /\      | |               | |                   / ____|                     
    /  \   __| __   _____ _ __ | |_ _   _ _ __ ___  | |  __  __ _ _ __ ___   ___ 
   / /\ \ / _` \ \ / / _ | '_ \| __| | | | '__/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \
  / ____ | (_| |\ V |  __| | | | |_| |_| | | |  __/ | |__| | (_| | | | | | |  __/
 /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|  \_____|\__,_|_| |_| |_|\___|
                                                                                 
                                                                                 
     """)



def villain_fight(mode,hp):
    hp_villian=0
    villain_data={}
    if mode=="e":
        villain=list(easy_villans.keys())
        fight_villain=random.choice(villain)
        villain_data=easy_villans[fight_villain]
        hp_villian = 1200
    elif mode=="m":
        villain = list(medium_villains.keys())
        fight_villain = random.choice(villain)
        villain_data = medium_villains[fight_villain]
        hp_villian=1500
    elif mode=="h":
        villain = list(hard_villans.keys())
        fight_villain = random.choice(villain)
        villain_data = hard_villans[fight_villain]
        hp_villian=1600

    count=0
    while hp>0 and hp_villian>0:
        print(f"""Player" Hp:::::::| {hp}  |\n  Villain Hp ::::::|{hp_villian}|""")
        random_attack=random.choice(villain_data["attacks"])
        for i in range (0,4):
           print( user_attacks[i][0])
        choose_attack=int(input("Type Number in front of them for attack"))
        hp-=random_attack[1]
        print(f"You Was attacked By attack {random_attack[0]} ")
        hp_villian-=user_attacks[choose_attack-1][1]
        print(f"Villain is attacked By attack {user_attacks[choose_attack-1][0]} ")

        if hp_villian<300 and count==0:
            count+=1
            hp_villian-=100
            print("A special Attacked launched")
    if hp>0:
        return True
    else:
        return False




is_continue=True
is_win=False
while is_continue:
    game_level=input("Which level of difficulty you want\n Easy\n Medium \n Hard\n Each level represent by first letter").lower()
    hp_player = 1000

    if game_level=="e"or game_level=="m" or game_level=="h":

        print(r"""
                    ╔════════════════════════╗
                    ║      ⚔ BATTLE ⚔        ║
                    ╠════════════════════════╣
                    ║      Fight Begins!     ║
                    ╚════════════════════════╝

                    """)

        is_win=(villain_fight(game_level,hp_player))
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
