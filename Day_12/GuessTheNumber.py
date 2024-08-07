from random import randint
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(guess, actual_number, attempts):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > actual_number:
    print("Too high.")
    return attempts - 1
  elif guess < actual_number:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {actual_number}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  actual_number = randint(1, 100)
  print(f"Pssst, the correct answer is {actual_number}") 

  attempts = set_difficulty()

  guess = 0
  while guess != actual_number:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    attempts = check_answer(guess, actual_number, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != actual_number:
      print("Guess again.")


game()

