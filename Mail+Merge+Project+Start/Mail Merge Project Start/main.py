#TODO: Create a letter using starting_letter.txt
PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt") as names_files:
    names=names_files.readlines()

#for each name in invited_names.txt
with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_files=letter_files.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_files.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed:
            completed.write(new_letter)


#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp