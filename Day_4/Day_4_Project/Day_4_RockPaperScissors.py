##### METHOD 1 #####

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = ["rock", "paper", "scissors"]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 3 or user_choice < 0: 
#     print("You typed an invalid number, you lose!")
# else:
#     print("You chose:")
#     print(game_images[user_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])

#     if user_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose")
#     elif computer_choice > user_choice:
#         print("You lose")
#     elif user_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == user_choice:
#         print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end









##### METHOD 2 #####

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

images = [rock, paper, scissors]
choices = ["rock", "paper", "scissors"]

print("ROCK, PAPER, SCISSORS")
print("Rules for playing Rock, Paper, Scissors:\n"
      "Rock wins against scissors.\n"
      "Scissors win against paper.\n"
      "Paper wins against rock.\n")

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer = random.randint(0, 2)

if player >= 3 or player < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose: {choices[player]}")
    print(images[player])
    print(f"Computer chose: {choices[computer]}")
    print(images[computer])

    if player == computer:
        print("It's a draw!")
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")




