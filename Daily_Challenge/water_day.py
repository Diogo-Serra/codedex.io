#!/usr/bin/env python3


def remaining_volume(volume, leak, hours, threshold):
    if volume < threshold:
        return -1

    for _ in range(hours):
        volume = volume * (1 - leak / 100)
        if volume < threshold:
            return -1

    return round(volume, 2)
