#!/usr/bin/env python3

phases_moon = [
    ("New Moon", "🌑"),
    ("Waxing Crescent", "🌒"),
    ("First Quarter", "🌓"),
    ("Waxing Gibbous", "🌔"),
    ("Full Moon", "🌕"),
    ("Waning Gibbous", "🌖"),
    ("Last Quarter", "🌗"),
    ("Waning Crescent", "🌘")]


def moon_phase(phase):
    for name, emoji in phases_moon:
        if phase == name:
            print(emoji)


moon_phase("New Moon")
