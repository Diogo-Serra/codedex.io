#!/usr/bin/env python3

def wordle_guess(secret, guess) -> int:
    # Your code here
    i = 0
    count = 0
    while i < 5:
        if secret[i] == guess[i]:
            count += 1
        i += 1
    return count


output = wordle_guess("HELLO", "WORLD")
print(f"Output: {output}")
