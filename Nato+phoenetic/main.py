import pandas

data=pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
word=input("Enter Your name").upper()

name=[phonetic_dict[letter] for letter in word]
print(name)