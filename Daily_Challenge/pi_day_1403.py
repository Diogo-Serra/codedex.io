#!/usr/bin/env python3
from math import pi


def cut_pie(diameter, friends):
    circ = round((pi * diameter) / friends, 2)
    return circ


res = cut_pie(10, 2)
print(res)
