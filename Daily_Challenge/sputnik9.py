#!/usr/bin/env python3
"""
The Earth's atmosphere is divided into five layers:
Exosphere (700-10,000 km): descent rate = 2000 m/s (near vacuum, free fall)
Thermosphere (85-700 km): descent rate = 500 m/s (thin air, minimal drag)
Mesosphere (50-85 km): descent rate = 200 m/s (air thickens, meteors burn here)
Stratosphere (12-50 km): descent rate = 75 m/s (ozone layer, much denser)
Troposphere (0-12 km): descent rate = 20 m/s
(densest layer, parachute deploys 🪂)
Sputnik 9's reentry begins from ~200 km. That's in the thermosphere.
The atmospheric density increases as the capsule descends...
the descent rate slows the lower it gets.
"""


def calculate_descent(altitude):
    layers = [
        (85,  700, 500),   # Thermosphere
        (50,   85, 200),   # Mesosphere
        (12,   50,  75),   # Stratosphere
        (0,    12,  20),   # Troposphere
    ]

    total_time = 0.0
    for bottom, top, rate in layers:
        if altitude <= bottom:
            continue
        entry = min(altitude, top)
        total_time += (entry - bottom) * 1000 / rate
        altitude = bottom

    return round(total_time, 1)


layer_names = [
    (85,  700, 500, "Thermosphere"),
    (50,   85, 200, "Mesosphere"),
    (12,   50,  75, "Stratosphere"),
    (0,    12,  20, "Troposphere 🪂"),
]

altitude = 200  # km, starting altitude of Sputnik 9

print("Sputnik 9 Reentry Simulation")
print("=" * 35)

tmp = altitude
for bottom, top, rate, name in layer_names:
    if tmp <= bottom:
        continue
    entry = min(tmp, top)
    time = (entry - bottom) * 1000 / rate
    print(f"{time:.1f}s ({name})")
    tmp = bottom

print(f"\nTotal: {calculate_descent(altitude)}s")
print("=" * 35)
print("Sputnik 9 has landed! 🛸")
