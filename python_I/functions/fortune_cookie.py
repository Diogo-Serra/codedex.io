#!/usr/bin/env python3
import random

list = [
    "Don't pursue happiness – create it.",
    "All things are difficult before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Someone in your life needs a letter from you.",
    "Don't just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! I'm being held prisoner in a Chinese bakery!"]


def fortune():
    f = random.randint(0, 7)
    match f:
        case 0:
            print(list[0])
        case 1:
            print(list[1])
        case 2:
            print(list[2])
        case 3:
            print(list[3])
        case 4:
            print(list[4])
        case 5:
            print(list[5])
        case 6:
            print(list[6])
        case 7:
            print(list[7])


fortune()
