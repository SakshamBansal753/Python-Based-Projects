
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print  (""" 
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88""")
def encrypt(original_text,shift_amount):
    Encrypted_Message=""
    sums=0
    original_text=original_text.lower()
    for letter in original_text:
        if letter in alphabet:
            Alpha_index=(alphabet.index(letter)+shift_amount)%len(alphabet)
            Encrypted_Message+=alphabet[Alpha_index]
        else:
            Encrypted_Message+=letter
    print(f"Your encoded message=> \n'{Encrypted_Message}'\nShare it secretly and also Your shift number")
def decode(original_text,shift_amount):
    plain_text=""

    original_text=original_text.lower()
    for letter in original_text:
        if letter in alphabet:
            Alpha_index=(alphabet.index(letter)-shift_amount)%len(alphabet)
            plain_text+=alphabet[Alpha_index]
        else:
         plain_text+=letter
    print(f"You message  that You want to decode is:\n{plain_text}\n See It Secretly")

#MAIN CODE IS HERE
user_name=input("Enter Your Name User ")
age=int(input("Enter Your Age"))
if age<=18:
    print(f"Hello Young master{user_name}")
else:
    print(f"Hello Sir {user_name}")
access=True
while  access:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
 if direction=="encode":
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encrypt(text,shift)

 else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decode(text,shift)
 yes_no=input("Enter y for continue and n for exit").lower()
 if yes_no=="n":
     access=False




