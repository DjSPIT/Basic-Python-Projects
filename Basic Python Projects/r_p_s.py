import random


def game():
    user = input("Choose from these three: 'R' for rock, 'P' for paper and 'S' for scissors\n")
    comp = random.choice(['R', 'P', 'S'])
    if user != 'R' and user != 'S' and user != 'P':
        print("Wrong Input Sorry.")
    else:
        print("The computer chooses:")
        print(comp)
        if user == comp:
            print("Its a Tie")
        elif win(user, comp):
            print("You have won!")
        else:
            print("You have lost!!!")


def win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (
            player == 'P' and opponent == 'R'):
        return True


game()
