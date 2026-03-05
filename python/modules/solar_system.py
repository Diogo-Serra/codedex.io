#!/usr/bin/env python3
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn']
random_planet = ch(planets)
if random_planet == 'Mercury':
    r = 2440
if random_planet == 'Venus':
    r = 6052
if random_planet == 'Earth':
    r = 6371
if random_planet == 'Mars':
    r = 3390
if random_planet == 'Saturn':
    r = 58232
area = round((4 * pi * r)**2)
print(f"{random_planet} - {area:,.2f}")
