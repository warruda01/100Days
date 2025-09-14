import random
# import my_module

# a = randint(1, 50)

# print(my_module.my_favorite_number)
# print(a)

# random_number_0_to_100 = random.random() * 10
# random_number_0_to_1 = random.random()
# random_number_111 = random.uniform(1, 100)
# print(random_number_0_to_1)
# print(random_number_0_to_100)
# print(random_number_111)


coin = random.randint(0, 1)
user = input("Heads or Tails? ").lower()
if user == "heads":
    user = 1
else:
    user = 0

if coin == user:
    if coin == 1:
        print('Coin: heads')
        print("You Win")
    else:
        print('Coin: tails')
        print("You Win")
else:
    if coin == 1:
        print("You got Heads")
        print("Better luck next time!")
    else:
        print("You got Tails")
        print("Better luck next time!")