import  random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Ask_input=int(input("What do You Choose ? Type 0 for Rock,1 for Paper or 2 for scissors"))
if Ask_input==0 or Ask_input==1 or Ask_input==2:


 RPS=[rock,paper,scissors]
 randomChoice=random.randint(0,2)

 if Ask_input==randomChoice:
    print(f" Computer chose \n {RPS[randomChoice]} Its A Draw ")
 elif (Ask_input==0 and randomChoice==2)or(Ask_input==1 and randomChoice==0) or(Ask_input==2 and randomChoice==1):
    print(f"Computer chooses \n {RPS[randomChoice]}\n You Win")
 else:
    print(f"Computer chooses \n {RPS[randomChoice]}\n You Lose")
else:
    print("Invalid")





