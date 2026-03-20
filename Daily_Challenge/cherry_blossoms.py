#!/usr/bin/env python3

def cherry_blossoms(temps):
    for i in range(4, len(temps)):
        avg = sum(temps[i-4:i+1]) / 5
        if avg > 15:
            return i + 1
    return -1


def tester():
    temperatures = [10, 11, 13, 14, 16, 17, 18]
    temperatures2 = [12, 14, 15, 16, 17, 11, 13]
    print(f"Example 1: {cherry_blossoms(temperatures)} (expected: 7)")
    print(f"Example 2: {cherry_blossoms(temperatures2)} (expected: -1)")


tester()
