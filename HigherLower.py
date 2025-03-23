import random
from art import logo
from game_data import data
import os

def win_condition(guess,a_acc,b_acc):
    if a_acc["follower_count"]>b_acc["follower_count"]:
        return guess=="a"
    else:
        return guess=="b"



score=0
game_is_continue=True
account_b = random.choice(data)
while game_is_continue:
    print(logo)


    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"😎A){account_a["name"]} having {account_a["description"]} from{account_a["country"]}")
    print("vs")
    print(f"😎B){account_b["name"]} having {account_b["description"]} from{account_b["country"]}")
    guess=input("Type A if A has more no of follower if not then B").lower()
    is_win=win_condition(guess,account_a,account_b)
    if is_win:
        print("👏You Are Correct")
        print("\n"*20)
        os.system("cls" if os.name == "nt" else "clear")

        score+=1
    else:
        print("😢You guessed wrong")


        game_is_continue=False

print(f"🏆Your Final Score is {score}🏆")
