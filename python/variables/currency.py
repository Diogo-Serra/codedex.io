#!/usr/bin/env python3

def currency():
    pesos = int(input("What do you have left in pesos? "))
    soles = int(input("What do you have left in soles? "))
    reais = int(input("What do you have left in reais? "))
    result = ((pesos * 0.00027) + (soles * 0.30) + (reais * 0.19))
    print(f"You have {round(result, 2)}$US")


currency()
