#!/usr/bin/env python3

def find_missing_colors(grid):
    all_colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

    # Flatten the grid into one list and convert to a set
    colors_in_grid = set(color for row in grid for color in row)

    # Find missing colors (keeping the original order)
    missing = [color for color in all_colors if color not in colors_in_grid]

    return missing
