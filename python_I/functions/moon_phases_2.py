#!/usr/bin/env python3

class MoonPhases():
    def __init__(self, phrase, emoji):
        self.phrase = phrase
        self.emoji = emoji

    def get_emoji(phases_moon, phrase):
        for phase in phases_moon:
            if phase.phrase == phrase:
                print(phase.emoji)


def moon_phase(phases_moon, phrase):
    MoonPhases.get_emoji(phases_moon, phrase)


phases_moon = [
    MoonPhases("New Moon", "🌑"),
    MoonPhases("Waxing Crescent", "🌒"),
    MoonPhases("First Quarter", "🌓"),
    MoonPhases("Waxing Gibbous", "🌔"),
    MoonPhases("Full Moon", "🌕"),
    MoonPhases("Waning Gibbous", "🌖"),
    MoonPhases("Last Quarter", "🌗"),
    MoonPhases("Waning Crescent", "🌘")]


moon_phase(phases_moon, "New Moon")
