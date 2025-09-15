import random
print('Welcome to the PyPassword Generator!')

password1 = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input('How many letters would you like in your password? '))
num_symbols = int(input('How many symbols would you like in your password? '))
num_numbers = int(input('How many numbers would you like in your password? '))

len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)

for l in range (0, num_letters):
    ind_letters = random.randint(0, len_letters-1)
    password1.append(letters[ind_letters])
for s in range (0, num_symbols):
    ind_symbols = random.randint(0, len_symbols-1)
    password1.append(symbols[ind_symbols])
for n in range (0, num_numbers):
    ind_numbers = random.randint(0, len_numbers-1)
    password1.append(numbers[ind_numbers])

password= random.shuffle(password1)
print(f"Your Password ==> {"".join(password1)}") #List to string


#Another way
password2 = ""
for l in range (0, num_letters):
    random_char = random.choice(letters)
    password2 += random_char
for s in range (0, num_symbols):
    random_sym = random.choice(symbols)
    password2 += random_sym
for n in range (0, num_numbers):
    random_num = random.choice(numbers)
    password2 += random_num




password2 = list(password2)
#print(f"Your Password ==> {password2}")
random.shuffle(password2)
print(f"Your Password ==> {"".join(password2)}")