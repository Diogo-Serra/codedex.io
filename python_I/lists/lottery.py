#!/usr/bin/env python3
from random import randint

my_numbers = []
winning_numbers = []
for i in range(0, 5):
    my_numbers.append(randint(1, 69))
    winning_numbers.append(randint(1, 69))
my_numbers.append(randint(1, 26))
winning_numbers.append(randint(1, 26))
print(my_numbers)
print(winning_numbers)
