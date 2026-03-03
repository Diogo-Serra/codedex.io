#!/usr/bin/env python3
"""
The year is 2199... Humanity is now an interplanetary species,
freely traveling across the solar system! 🚀

Create a weight conversion program that:

Asks the user for their Earth weight (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate
the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14
If the user enters a planet number outside of 1 - 7,
print a message that says 'Invalid number'
"""
earth_weight = float(input("Your Earth weight: "))
planet_number = int(input("Planet number: "))
destination_weight = 0.0
if planet_number == 1:
    destination_weight = earth_weight * 0.38
elif planet_number == 2:
    destination_weight = earth_weight * 0.91
elif planet_number == 3:
    destination_weight = earth_weight * 0.38
elif planet_number == 4:
    destination_weight = earth_weight * 2.53
elif planet_number == 5:
    destination_weight = earth_weight * 1.07
elif planet_number == 6:
    destination_weight = earth_weight * 0.89
elif planet_number == 7:
    destination_weight = earth_weight * 1.14
else:
    print("Invalid number")
