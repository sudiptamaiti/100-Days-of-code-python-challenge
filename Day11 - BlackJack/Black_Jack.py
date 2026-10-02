import random
from art import logo
#print(logo)


# 4 - to return a random card.
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
# 6 -
def calculate_score(cards):
    #7 check for blackjack,  "0" --> BLACKJACK
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    #8 if ACE(11) in the selected cards and score is over 21, change ACE(11) to 1
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#13-
def compare(u_score, c_score):
    if c_score==u_score:
        return"IT'S A DRAW!!"
    elif c_score==0 :
        return "YOU LOSE!!,Opponent has Blackjack"
    elif u_score==0 :
        return "YOU WINS!! with a Blackjack"
    elif u_score>21:
        return "You went over. You lose!!"
    elif c_score>21:
        return "Opponent went over. You win!!"
    elif u_score>c_score:
        return "YOU WIN!!"
    else:
        return "YOU LOSE!!"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1
    is_game_over=False

    #5- Deal the user and computer 2 cards
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        #9 - check game should end or not
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            #10
            choice=input("Type 'y' to get another card, type 'n' to pass: ")
            if choice=="y":
                user_cards.append(deal_cards())
            else:
                is_game_over= True
    #12 Computer's turn to play
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand:{user_cards}, final score:{user_score}")
    print(f"Computer's final hand:{computer_cards}, final score:{computer_score} ")
    print(compare(user_score,computer_score))

while(True):
    selected=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if selected=="y":
        print("\n" * 20)
        play_game()
    else:
        break

