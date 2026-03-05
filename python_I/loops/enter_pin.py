#!/usr/bin/env python3

# Write code below 💖
print('BANK OF CODEDEX')

pin = int(input("Enter your PIN: "))

while pin != 1234:
    pin = int(input("Incorrect PIN. Enter your PIN again: "))

if pin == 1234:
    print("PIN accepted")
