#!/usr/bin/env python3
from random import randint

player = int(input("\n1 - ✊\n2 - ✋\n3 - ✌️\nPick a number:"))
computer = randint(1, 3)
print("You chose:", end=' ')
if player == 1:
    print("✊")
if player == 2:
    print("✋")
if player == 3:
    print("✌️")
print("CPU chose:", end=' ')
if computer == 1:
    print("✊")
if computer == 2:
    print("✋")
if computer == 3:
    print("✌️")
if player != computer:
    if player == 1:
        if computer == 2:
            print("The computer won")
        elif computer == 3:
            print("The player won")
    elif player == 2:
        if computer == 1:
            print("The player won")
        elif computer == 3:
            print("The computer won")
    elif player == 3:
        if computer == 1:
            print("The computer won")
        elif computer == 2:
            print("The player won")
else:
    print("It's a tie!")
