#!/usr/bin/env python3
"""
The Earth's atmosphere is divided into five layers:
Exosphere (700-10,000 km): descent rate = 2000 m/s (near vacuum, free fall)
Thermosphere (85-700 km): descent rate = 500 m/s (thin air, minimal drag)
Mesosphere (50-85 km): descent rate = 200 m/s (air thickens, meteors burn here)
Stratosphere (12-50 km): descent rate = 75 m/s (ozone layer, much denser)
Troposphere (0-12 km): descent rate = 20 m/s (densest layer, parachute deploys 🪂)
Sputnik 9's reentry begins from ~200 km. That's in the thermosphere. The atmospheric density increases as the capsule descends... the descent rate slows the lower it gets.
"""

def calculate_descent(altitude):
    if altitude < 12:
        return 20    # Troposphere
    elif altitude < 50:
        return 75    # Stratosphere
    elif altitude < 85:
        return 200   # Mesosphere
    elif altitude < 700:
        return 500   # Thermosphere
    else:
        return 2000  # Exosphere


altitude = 200  # km, starting altitude of Sputnik 9

print("Sputnik 9 Reentry Simulation")
print("=" * 35)

while altitude > 0:
    rate = calculate_descent(altitude)

    if altitude >= 700:
        layer = "Exosphere"
    elif altitude >= 85:
        layer = "Thermosphere"
    elif altitude >= 50:
        layer = "Mesosphere"
    elif altitude >= 12:
        layer = "Stratosphere"
    else:
        layer = "Troposphere 🪂"

    print(f"Altitude: {altitude:6.1f} km | Layer: {layer:<18} | Descent rate: {rate} m/s")
    altitude -= rate / 1000  # convert m/s to km per step

print("=" * 35)
print("Sputnik 9 has landed! 🛸")
