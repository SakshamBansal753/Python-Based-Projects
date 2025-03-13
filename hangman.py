import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["carrot", "onion", "radish","pea"]
print("********  WELCOME TO THE HANGMAN GAME  ******* ")
print("""||  ||     
         ||  ||      -----------
         ||  ||          || 
         ||  ||          || 
         ||--||          || 
         ||--||          || 
         ||  ||          || 
         ||  ||      ----------- """)

lives=6
randomvalue=random.randint(0,len(word_list)-1)
chosen_word=word_list[randomvalue]


Question=["Its A veggie starts with c","Its A veggie starts with o","Its A veggie starts with r","Its A veggie starts with p"]
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"


game_over = False
correct_letters = []
name=input("Write Your Name User Please ==>")
age=int(input("Enter Your Age==>"))
if age<=18:
    print(f"Hello Young master {name}\nYou Have 6 lives \n{placeholder}")
else:
    print(f"Hello Sir {name}\nYou Have 6 lives \n{placeholder}")

print(f"Hint For You IS \n{Question[randomvalue]}")
while not game_over :
    print(f"lives=={lives}")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        print(f"You Have {lives} lives  left")
        if lives==0:
            game_over=True
            print("**********!You Loose!**********")
    else:

        for letter in chosen_word:
          if letter == guess:
            display += letter
            correct_letters.append(guess)
          elif letter in correct_letters:
            display += letter
          else:
            display += "_"
        print(display)
        if "_" not in display:
         game_over = True
         print("***************You win.***************")

