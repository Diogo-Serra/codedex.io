#!/usr/bin/env python3
import random

dye1 = random.randint(1, 6)
dye2 = random.randint(1, 6)
total = dye1 + dye2
while total != 2:
    dye1 = random.randint(1, 6)
    dye2 = random.randint(1, 6)
    total = dye1 + dye2
    print("Nope")
print("Snake eyes!")
