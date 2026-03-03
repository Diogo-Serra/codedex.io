#!/usr/bin/env python3
import random

dye1 = 0
dye2 = 0
while dye1 != 1:
    dye1 = random.randint(1, 6)
    print("Nope")
    while dye2 != 1:
        dye2 = random.randint(1, 6)
        print("Nope")
print("Snake eyes!")
