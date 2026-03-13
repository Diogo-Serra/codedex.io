#!/usr/bin/env python3

def check_palindrome(sequence: str) -> bool:
    sequence = "".join(sequence.lower().split())
    i: int = 0
    j: int = len(sequence) - 1
    while i < j:
        if sequence[i] != sequence[j]:
            return False
        i += 1
        j -= 1
    palindrome = True
    return (palindrome)


p = check_palindrome("Was it a car or a cat I saw")
print(p)
