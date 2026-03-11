#!/usr/bin/env python3
from itertools import combinations


def minimum_components(nums):
    for size in range(1, len(nums) + 1):
        for combo in combinations(nums, size):
            if sum(combo) == 42:
                return size
    return -1
