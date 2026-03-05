#!/usr/bin/env python3
import random


def magic8():
    magic = random.randint(0, 8)
    match magic:
        case 0:
            print("Yes - definitely.")
        case 1:
            print("It is decidedly so.")
        case 2:
            print("Without a doubt.")
        case 3:
            print("Reply hazy, try again.")
        case 4:
            print("Ask again later.")
        case 5:
            print("Better not tell you now.")
        case 6:
            print("My sources say no.")
        case 7:
            print("Outlook not so good.")
        case 8:
            print("Very doubtful.")


magic8()
