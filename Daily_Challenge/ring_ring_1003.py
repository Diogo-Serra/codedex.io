#!/usr/bin/env python3
import string


def find_unique_words(transcript):
    words = set()
    count = 0
    for i in transcript.split():
        if i:
            words.add(i.strip(string.punctuation).lower())
    for i in words:
        count += 1
    return count


message = "Hello Neil and Buzz, I am talking to you by telephone"
words = find_unique_words(message)
print((words))
