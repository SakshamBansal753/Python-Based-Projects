print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Base prices
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:  # Assuming "L"
    bill += 25

# Pepperoni cost
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Small pizza pepperoni cost
    else:
        bill += 3  # Medium & Large pizza pepperoni cost

# Extra cheese cost
if extra_cheese == "Y":
    bill += 1

# Print final bill
print(f"Your final bill is: ${bill}.")
