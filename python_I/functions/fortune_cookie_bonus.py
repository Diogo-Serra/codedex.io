#!/usr/bin/env python3
import random


class Phrases:
    def __init__(self, index, phrase):
        self.index = index
        self.phrase = phrase

    def get_phrase(my_phrases, index) -> str:
        for phrase in my_phrases:
            if phrase.index == index:
                return phrase.phrase


my_phrases = [
    Phrases(0, "Don't pursue happiness - create it."),
    Phrases(1, "All things are difficult before they are easy."),
    Phrases(2, "The early bird gets the worm, but the second mouse"
               " gets the cheese."),
    Phrases(3, "Someone in your life needs a letter from you."),
    Phrases(4, "Don't just think. Act!"),
    Phrases(5, "Your heart will skip a beat."),
    Phrases(6, "The fortune you search for is in another cookie."),
    Phrases(7, "Help! I'm being held prisoner in a Chinese bakery!")]
print(Phrases.get_phrase(my_phrases, random.randint(0, 7)))
