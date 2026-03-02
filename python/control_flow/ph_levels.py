#!/usr/bin/env python3

def validate_ph(ph):
    if ph < 0 or ph > 14:
        print("Invalid ph")
        exit()


def ph_levels():
    ph = int(input("Enter ph(0 - 14)"))
    validate_ph(ph)
    if ph > 7:
        print("Basic")
    elif ph < 7:
        print("Acidic")
    else:
        print("Neutral")


ph_levels()
