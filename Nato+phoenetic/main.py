import pandas

data=pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

is_ok=True
while  is_ok:
    word = input("Enter Your name").upper()
    try:
        name = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry Enter words only")
        is_ok=True
    else:
        print(name)
        is_ok = False


