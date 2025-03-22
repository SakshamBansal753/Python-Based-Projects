print(r""" /$$   /$$/$$   /$$/$$      /$$/$$$$$$$ /$$$$$$$$/$$$$$$$         /$$$$$$ /$$   /$$/$$$$$$$$ /$$$$$$  /$$$$$$ /$$$$$$/$$   /$$ /$$$$$$ 
        | $$$ | $| $$  | $| $$$    /$$| $$__  $| $$_____| $$__  $$       /$$__  $| $$  | $| $$_____//$$__  $$/$$__  $|_  $$_| $$$ | $$/$$__  $$
        | $$$$| $| $$  | $| $$$$  /$$$| $$  \ $| $$     | $$  \ $$      | $$  \__| $$  | $| $$     | $$  \__| $$  \__/ | $$ | $$$$| $| $$  \__/
        | $$ $$ $| $$  | $| $$ $$/$$ $| $$$$$$$| $$$$$  | $$$$$$$/      | $$ /$$$| $$  | $| $$$$$  |  $$$$$$|  $$$$$$  | $$ | $$ $$ $| $$ /$$$$
        | $$  $$$| $$  | $| $$  $$$| $| $$__  $| $$__/  | $$__  $$      | $$|_  $| $$  | $| $$__/   \____  $$\____  $$ | $$ | $$  $$$| $$|_  $$
        | $$\  $$| $$  | $| $$\  $ | $| $$  \ $| $$     | $$  \ $$      | $$  \ $| $$  | $| $$      /$$  \ $$/$$  \ $$ | $$ | $$\  $$| $$  \ $$
        | $$ \  $|  $$$$$$| $$ \/  | $| $$$$$$$| $$$$$$$| $$  | $$      |  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$|  $$$$$$//$$$$$| $$ \  $|  $$$$$$/
        |__/  \__/\______/|__/     |__|_______/|________|__/  |__/       \______/ \______/|________/\______/ \______/|______|__/  \__/\______/ 
                                                                                           
                                                                                                      """)

import random
while True:
    game_mode = input("Select Easy or Hard Mode: Type 'e' for Easy or 'h' for Hard: ").lower()
    if game_mode == "e":
        Lives = 6
        break
    elif game_mode == "h":
        Lives = 4
        break
    else:
        print("Invalid selection. Please type 'e' or 'h'.")
win_number=random.randint(1,100)
def check_is_win(win):
    global Lives
    global  win_number

    if Lives!=0:
        if win==win_number:
            print("🎉 You Win! 🎉 ")
            return True
        elif win<win_number:
            print("📉 Too Low! Try a higher number. ")
            Lives-=1
            return False
        else:
            print("📈 Too High! Try a lower number.")
            Lives-=1
            return False
    else:
        print(f"💀 You Lost!  The Correct Number Is {win_number}")
        return True
is_true=False
while not is_true:
    guess_number=int(input("Enter the  Number"))
    if 1< guess_number <100:
        is_true=check_is_win(guess_number)
    else:
        print("Invalid ")
