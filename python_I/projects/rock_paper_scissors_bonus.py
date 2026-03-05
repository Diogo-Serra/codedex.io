#!/usr/bin/env python3
from random import randint

player = int(input("\n1 - ✊\n2 - ✋\n3 - ✌️\n4 - 🦎\n5 - 🖖\nPick a number: "))
computer = randint(1, 5)

print("You chose:", end=' ')
if player == 1:
    print("✊")
elif player == 2:
    print("✋")
elif player == 3:
    print("✌️")
elif player == 4:
    print("🦎")
elif player == 5:
    print("🖖")

print("CPU chose:", end=' ')
if computer == 1:
    print("✊")
elif computer == 2:
    print("✋")
elif computer == 3:
    print("✌️")
elif computer == 4:
    print("🦎")
elif computer == 5:
    print("🖖")

if player != computer:
    if player == 1:
        if computer == 3 or computer == 4:
            print("The player won")
        else:
            print("The computer won")
    elif player == 2:
        if computer == 1 or computer == 5:
            print("The player won")
        else:
            print("The computer won")
    elif player == 3:
        if computer == 2 or computer == 4:
            print("The player won")
        else:
            print("The computer won")
    elif player == 4:
        if computer == 2 or computer == 5:
            print("The player won")
        else:
            print("The computer won")
    elif player == 5:
        if computer == 1 or computer == 3:
            print("The player won")
        else:
            print("The computer won")
else:
    print("It's a tie!")
