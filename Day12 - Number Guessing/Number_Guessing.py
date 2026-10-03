import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_num=random.randint(1,100)
choice=input("Choose difficulty. Type 'easy' or 'hard' : ").lower()
wants_to_continue=True
if choice=="easy":
    attempts=10
else:
    attempts=5
while attempts>0:

    guess=int(input("Make a guess: "))
    if (guess == random_num):
        print(f"You got it! The answer was {random_num}")
        break
    elif guess>random_num:
            print("Too high.\nGuess again.")
            attempts-=1
            print(f" You have {attempts} attempts remaining to guess the number.")
    else :
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f" You have {attempts} attempts remaining to guess the number.")



