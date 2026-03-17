#!/usr/bin/env python3


def lucky_river(river, hours):
    for i, area in enumerate(river[:]):
        if area == '☘️':
            for j in range(hours + 1):
                if i + j < len(river):
                    river[i + j] = '☘️'
    return river


def tester():
    river = ['💧', '☘️', '💧', '💧', '💧', '☘️', '💧', '💧']
    hours = 1
    result = lucky_river(river, hours)
    print(f"Result: {result}")
    print("Expected: ['💧', '☘️', '☘️', '💧', '💧', '☘️', '☘️', '💧']")


tester()
