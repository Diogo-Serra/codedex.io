#!/usr/bin/env python3

class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, points):
        self.points += points


teams = [
    Team("Slytherin", 0),
    Team("Hufflepuff", 0),
    Team("Ravenclaw", 0),
    Team("Gryffindor", 0)]


def get_team(name):
    for team in teams:
        if team.name == name:
            return team


def sorting_hat():
    print("Q1) Do you like Dawn or Dusk?")
    print("     1) Dawn")
    print("     2) Dusk")
    question = int(input())
    if question == 1:
        get_team("Gryffindor").add_points(1)
        get_team("Ravenclaw").add_points(1)
    elif question == 2:
        get_team("Hufflepuff").add_points(1)
        get_team("Slytherin").add_points(1)
    print("Q2) When I’m dead, I want people to remember me as:")
    print("    1) The Good")
    print("    2) The Great")
    print("    3) The Wise")
    print("    4) The Bold")
    question = int(input())
    if question == 1:
        get_team("Hufflepuff").add_points(2)
    elif question == 2:
        get_team("Slytherin").add_points(2)
    elif question == 3:
        get_team("Ravenclaw").add_points(2)
    elif question == 4:
        get_team("Gryffindor").add_points(2)
    print("Q3) Which kind of instrument most pleases your ear?")
    print("    1) The violin")
    print("    2) The trumpet")
    print("    3) The piano")
    print("    4) The drum")
    question = int(input())
    if question == 1:
        get_team("Slytherin").add_points(4)
    elif question == 2:
        get_team("Hufflepuff").add_points(4)
    elif question == 3:
        get_team("Ravenclaw").add_points(4)
    elif question == 4:
        get_team("Gryffindor").add_points(4)


sorting_hat()
for team in teams:
    print(f"{team.name} : {team.points}\n")


winner = teams[0]
for team in teams:
    if team.points > winner.points:
        winner = team
print(f"You belong to: {winner.name}")
