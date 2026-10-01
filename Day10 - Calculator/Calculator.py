import art
#print(art.logo)
def add(n1, n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(art.logo)
    wants_to_continue=True

    n1 = float(input("What's the first number?: "))
    while wants_to_continue:
        for symb in operation:
            print(symb)

        symbol = input("Pick an operation: ")

        n2 = float(input("What's the second number?: "))
        answer=operation[symbol](n1, n2) # A dictionary lets you directly access a value using its key, so you don't need a loop to search for that key.
        print(f"{n1} {symbol} {n2} = {answer}")  # A dictionary lets you directly access a value using its key, so you don't need a loop to search for that key.

        yes_or_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()


        if yes_or_no=="y":
            n1=answer

        else:
            wants_to_continue=False
            print("\n"*20)
            calculator()
calculator()


