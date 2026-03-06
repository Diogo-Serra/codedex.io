#!/usr/bin/env python3

def calculate_score(elements):
    tes = 0.0
    for element in elements:
        name, base, goe = element
        goe_scores = sorted(goe)
        trimmed = goe_scores[1:-1]  # drop lowest and highest
        avg_goe = sum(trimmed) / len(trimmed)
        element_score = base + (avg_goe * 0.1 * base)
        tes += element_score
    return round(tes, 1)


elements = [
    ("Triple Flip", 9.7, [3, 2, 3, 3, 2, 4, 3, 2, 3]),
    ("Triple Lutz+Toe Combo", 12.5, [4, 5, 4, 5, 5, 4, 4, 3, 4]),
    ("Triple Salchow", 7.0, [2, 3, 2, 2, 3, 2, 2, 3, 2]),
    ("Triple Loop", 6.0, [3, 3, 2, 4, 3, 3, 2, 3, 2]),
    ("Step Sequence", 3.3, [4, 4, 4, 4, 3, 3, 4, 3, 4]),
]

print(calculate_score(elements))
