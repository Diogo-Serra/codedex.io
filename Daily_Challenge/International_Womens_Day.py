#!/usr/bin/env python3

def analyze(percentages):
    net_change_per_year = round((percentages[-1] - percentages[0]) / (len(percentages) - 1), 4)

    first_avg = sum(percentages[:3]) / 3
    last_avg = sum(percentages[-3:]) / 3
    if last_avg > first_avg:
        trend = "improving"
    elif last_avg == first_avg:
        trend = "stagnating"
    else:
        trend = "declining"

    dips = sum(1 for i in range(1, len(percentages)) if percentages[i] < percentages[i - 1])

    return net_change_per_year, trend, dips


# Meta (2014-2022)
print(analyze([31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]))

# Amazon (2014-2024)
print(analyze([42.0, 43.0, 42.0, 43.0, 44.0, 44.0, 44.6, 44.8, 44.7, 45.0, 45.8]))

# Apple (2014-2024)
print(analyze([30.0, 31.0, 32.0, 32.0, 33.0, 34.0, 34.0, 34.8, 35.0, 35.0, 35.3]))
