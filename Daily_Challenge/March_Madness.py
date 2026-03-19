#!/usr/bin/env python3

def upset_probability(matchups):
    output_upset = []
    for match in matchups:
        x = match[1]
        y = match[3]
        if x > y:
            rounded = round(x / (x + y), 2)
            output_upset.append(rounded)
        else:
            rounded = round(x / (x + y), 2)
            output_upset.append(rounded)
    return (output_upset)


def tester():
    matchups = [
        ["Duke", 1, "Siena", 16],
        ["Ohio State", 8, "TCU", 9]]
    print(upset_probability(matchups))


tester()
