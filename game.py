import random
print("----------------------------------Snake ,Water,Gun-------------------------------")



while True :
    no = random.randint(0,2)
    if no == 0 :
        choice = "Snake"
    elif no == 1 :
        choice = "Water"
    elif no == 2 :
        choice = "Gun"

    print("user options :-")
    print("1 :- snake")
    print("2 :- water")
    print("3 :- gun")
    print("4 :- Exit")
    b =int(input("Enter your choice :- "))

    if b == 1 :
        choice1 = "Snake"
    elif b == 2 :
        choice1 = "Water"
    elif b == 3 :
        choice1 = "Gun"
    elif b == 4 :
        break
    

    if (no == 0) and (b == 3):
        print("You won")
    elif (no == 1) and (b == 1):
        print("You won")
    elif (no == 2) and (b == 2):
        print("You won")

    elif (no == 0) and (b == 2):
        print("You lose")
    elif (no == 1) and (b == 3):
        print("You lose")
    elif (no == 2) and (b == 1):
        print("You lose")

    elif (no == 0) and (b == 1):
        print("Tie")
    elif (no == 1) and (b == 2):
        print("Tie")
    elif (no == 2) and (b == 3):
        print("Tie")

    print(f"Your choice :- {choice1} \nMy choice :- {choice} \n\n\n")