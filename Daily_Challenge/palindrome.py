#!/usr/bin/env python3

def check_palindrome(sequence: str) -> bool:
# Write code below 💖
    i: int = 0
    j: int = len(sequence) - 1
    while i < j:
        if sequence[i] != sequence[j]:
            return False
        i += 1
        j -= 1
    palindrome = True
    return (palindrome)


p = check_palindrome("car")
print(p)
