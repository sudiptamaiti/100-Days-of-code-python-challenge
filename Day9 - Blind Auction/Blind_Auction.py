from art import logo
print(logo)

def max_bid(bidding_dict):
    #maxi = max(bidding_dict, key=bidding_dict.get)
    #or
    highest_bid=0
    winner=""
    for name in bidding_dict:
        if bidding_dict[name]>highest_bid:
            highest_bid=bidding_dict[name]
            winner=name
    print(f"The winner is {winner} with a bid of ${highest_bid}")


dict_1={}
continue_bidding=True

while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))
    dict_1[name] = price
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    if yes_or_no=="no":
        continue_bidding=False
        max_bid(dict_1)
    elif yes_or_no=="yes":
        print("\n"*20)




