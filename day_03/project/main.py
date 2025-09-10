print("""
      treasure chest:
         __________
        /\____;;___\/
       | /         /
       `. ())oo() .
        |\(%()*^^()^\/
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
""")
print("""Welcome to the Treasure Island
Your mission is to fin the treasure.
You are at a cross road. Where do you want to go?""")
choice_1 = input("Type 'left' or 'right' --> ").lower()

if choice_1 == 'right':
    message = 'Fall into a hole. Game over.'
elif choice_1 == 'left':
    print(10 * '-')
    print("""You've come to a lake. There is an island in the middle of the lake.
Type 'wait' to wait for a boat. Type 'swim' to swim across.""")
    choice_2 = input("Type 'wait' or 'swim' --> ").lower()

    if choice_2 == 'swim':
        message = 'Attacked by trout. Game Over.'
    elif choice_2 == 'wait':
            print(10 * '-')
            print("""You arrive at the island unharmed. There's a house with 3 doors.
One red.
One yellow.
One blue. """)
            choice_3 = input("Which door? Type 'blue', 'red' or 'yellow' --> ").lower()

            if choice_3 == 'red':
                message = 'Burned by fire. Game Over.'
            elif choice_3 == 'blue':
                message = 'Eaten by beasts. Game Over.'
            elif choice_3 == 'yellow':
                message = 'YOU WIN.'
            else:
                message = 'Game Over.'
    else:
        message = 'Attacked by trout. Game Over.'
else:
    message = 'Fall into a hole. Game Over.'

print(message)
