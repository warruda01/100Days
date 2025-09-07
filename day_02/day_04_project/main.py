print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? % - 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total_tip = (total * tip) / 100
split = (total + total_tip)/people

print(f"Each person should pay: $ {split:.2f}")

