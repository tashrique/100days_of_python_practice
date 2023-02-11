import random

# Defining ASCII shapes
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

# taking user input and printig the corresponsing move
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
game_moves = [rock, paper, scissors]
print(game_moves[user_input])

# generating computer input and printing the corresponding move
random_num = random.randint(0, 2)
print("Computer chose: \n")
print(game_moves[random_num])

# conditions to check who won the game
if user_input == random_num:
	print("It's a draw!")
elif user_input == 0 and random_num == 1:
	print("You lost!")
elif user_input == 0 and random_num == 2:
	print("You win!")
elif user_input == 1 and random_num == 0:
	print("You win!")
elif user_input == 1 and random_num == 2:
	print("You lost!")
elif user_input == 2 and random_num == 0:
	print("You lost!")
elif user_input == 2 and random_num == 1:
	print("You win!")
else:
	print("You lost. Try again!")

