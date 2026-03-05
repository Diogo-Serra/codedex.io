#!/usr/bin/env python3
import random

symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
result = random.choices(symbols, k=3)
print(f"{result[0]} | {result[1]} | {result[2]}")
if result[0] == result[1] == result[2] == '7️⃣':
    print("Jackpot! 💰")


def play():
    again = input("Play again?(Y/N): ")
    while again == 'Y':
        result = random.choices(symbols, k=3)
        print(f"{result[0]} | {result[1]} | {result[2]}")
        if result[0] == result[1] == result[2] == '7️⃣':
            print("Jackpot! 💰")
        again = input("Play again?(Y/N): ")
    exit()


play()
