#!/usr/bin/env python3

class Pokemon():
    def __init__(self, entry, name, level, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.level = level
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name * 2)

    def display_details(self):
        print(f"Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"Podedex: {self.name} has already been caught")
        else:
            print(f"{self.name} still not caught")
