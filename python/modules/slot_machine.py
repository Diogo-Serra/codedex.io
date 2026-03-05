#!/usr/bin/env python3
import random

symbols = ['🍒', ' 🍇', '🍉', '7️']

result = random.choices(symbols, k=3)
print(f"{result[0]} | {result[1]} | {result[2]}")
