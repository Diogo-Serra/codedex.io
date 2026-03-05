#!/usr/bin/env python3

def dog_years(name, age):
    age = age * 7
    return (f"{name} is {age} years old in human years.")


dog = dog_years("Kovu", 6)
print(dog)
