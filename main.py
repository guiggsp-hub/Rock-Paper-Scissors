import random
computer =random.randint(1,3)

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

print('Welcome to the Rock, Paper, Scissors game!')
player=int(input('What do you choose?\n[1]Rock\n[2]Paper\n[3]Scissors\n------> '))

if player == 1:
    print(rock)
if player ==2:
    print(paper)
if player ==3:
    print(scissors)

if computer == 1:
    print('The computer chose Rock')
    print(rock)
if computer ==2:
    print('The computer chose Paper')
    print(paper)
if computer ==3:
    print('The computer chose Scissors')
    print(scissors)

if player == 1 and computer == 2:
    print ('Game Over!!')
elif player == 1 and computer == 3:
    print('You win!')
elif player == 2 and computer == 3:
    print ('Game Over!')
elif player == 2 and computer ==1:
    print('You win!')
elif player == 3 and computer == 1:
    print('Game Over!')
elif player == 3 and computer == 2:
    print('You win!')
if player == computer:
    print('Draw!')
