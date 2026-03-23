#!/usr/bin/env python3


def cuddly_kittens(kittens, limit):
    longest = 0

    for left in range(len(kittens)):
        current_min = kittens[left]
        current_max = kittens[left]

        for right in range(left, len(kittens)):
            current_min = min(current_min, kittens[right])
            current_max = max(current_max, kittens[right])

            if current_max - current_min <= limit:
                longest = max(longest, right - left + 1)
            else:
                break

    return longest
