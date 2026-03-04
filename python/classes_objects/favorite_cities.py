#!/usr/bin/env python3

class City():
    def __init__(
        self,
        nickname: str,
        name: str,
        country: str,
        population: int,
        landmarks: list,
    ):
        self.nickname = nickname
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


hometown = City("Teste", "Lisbon", "Portugal", 8000000, ["Teste", "Teste"])
tovisit = City("Teste", "Rome", "Italy", 23000000, ["Teste", "Teste"])
print(vars(hometown))
