print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza to you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0
if size == 'S':
    bill += 5
elif size == 'M':
    bill = 7
elif size == 'L':
    bill = 9
else:
    print("You typed the wrong inputs.")

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

print(f"Total bill: ${bill}")
