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

def game():
    list=["Rock","Paper","Scissor"]

    wants_to_continue=True

    while wants_to_continue:

        user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.--> "))

        if user_choice>=0 and user_choice<=2:
            print(f" User Choice {list[user_choice]}")

        computer_choice= random.randint(0,2)
        print(f"Computer Choice {list[computer_choice]}")

        if user_choice< 0 and user_choice>2:
            print("INVALID CHOICE!!. YOU LOSE!!")
        elif user_choice==0 and computer_choice == 2:
            print("You wins!")
        elif computer_choice==0 and user_choice==2:
            print("You loose")
        elif computer_choice> user_choice:
            print("You loose")
        elif user_choice>computer_choice:
            print("You win")
        else:
            print("It's a DRAW")

        yes_or_no=input("Do you want to play again ? (yes/no) : ").lower()

        if yes_or_no!="yes":
            wants_to_continue=False

game()

