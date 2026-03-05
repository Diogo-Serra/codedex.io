#!/usr/bin/env python3

guess = 0
tries = 0
while guess != 6:
    while tries < 4:
        guess = int(input("Guess the number:  "))
        tries += 1
    exit()
print("You got it!")
