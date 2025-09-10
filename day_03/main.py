print("Welcome to the rollecoster!")
height = int(input("What is yout height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif 12 <= age <=18:
        bill = 7
    elif age >= 18:
        bill = 12
    elif age >=45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        print("You typed a wrong input")
    
    foto = input("Do you want a foto (Y/N) ? ").upper()
    if foto in 'Y':
        bill += 3

    print(f'Total bill is {bill}')

else:
    print("Sorry you have to grow taller before you can ride.")
