# the snake water gun game:
import random
def game():
    choice = int(input(" select an option: \n 1 : snake, 0 : water,-1 : gun  \n  "))
    gamedict = {
        1 : "snake",
        0 : "water",
        -1 : "gun"
    }
    computer = random.choice([-1, 0, 1])
    print(f"\nYou chose {gamedict[choice]} and\n Computer chose {gamedict[computer]}")

    if computer == choice:
        print("the game is draw")

    else:
        if computer==-1 and choice == 0:
            print("You Win")
        elif computer==-1 and choice == 1:
            print("You loose")
        elif computer==1 and choice == -1:
            print("You Win")
        elif computer==1 and choice == 0:
            print("You loose")
        elif computer==0 and choice == -1:
            print("You loose")
        elif computer==0 and choice == 1:
            print("You Win")

        else:
            print("invalid selction ")

game()