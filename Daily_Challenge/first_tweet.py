#!/usr/bin/env python3
import unicodedata


def tweet_balance(tweet):
    balance = 140
    words = tweet.split()
    spaces = tweet.count(" ")
    balance -= spaces
    for word in words:
        if word.startswith("@"):
            balance -= 20
        elif word.startswith("http://") or word.startswith("https://"):
            balance -= 23
        else:
            for ch in word:
                if unicodedata.category(ch).startswith("So"):
                    balance -= 2
                else:
                    balance -= 1
    return balance


def tester():
    tests = [
        "Check out this link https://www.averylongurlthatgoesonnnnnn.com and this one https://short.co too!",
        "Wow I really cannot believe how much I have to say today, there are just so many things going on in my life right now and I really need to tell everyone about all of it immediately!!",
        "hey @codedex_io what's tomorrow's challenge?"
    ]
    for test in tests:
        result = tweet_balance(test)
        print(f"Input: {test}")
        print(f"Result: {result}")
        print()


tester()
