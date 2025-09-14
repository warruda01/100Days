import random
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input('What is your choice? ').lower()
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)

while True:

    print(f'You choose: {player.upper()}')
    if player == 'rock':

        print(rock)


    if player == 'paper':

        print(paper)

    if player == 'scissors':

        print(scissors)


    #Computer choice:

    print(f"Computer Choice: {computer.upper()}")
    if computer == 'rock':

        print(rock)


    if computer == 'paper':

        print(paper)

    if computer == 'scissors':

        print(scissors)

    if player == computer:
        print('Try again')
        player = input('What is your choice? ').lower()
        choices = ['rock', 'paper', 'scissors']
        computer = random.choice(choices)

    else:
        break

if player == 'rock' and computer == 'scissors':
    print('You Win')
elif player == 'rock' and computer == 'paper':
    print('You Lose')
elif player == 'scissors' and computer == 'paper':
    print('You Win')
elif player == 'scissors' and computer == 'rock':
    print('You Lose')
elif player == 'paper' and computer == 'rock':
    print('You Win')
elif player == 'paper' and computer == 'scissors':
    print('You Lose')
