#!/usr/bin/env python3
import datetime


# 2 hours and 48 minutes apart
def blood_moon(time):
    my_timestamps = []
    now = datetime.datetime.strptime(time, "%H:%M")
    later = now + datetime.timedelta(hours=2, minutes=48)
    my_timestamps.append(later)
    later = later + datetime.timedelta(hours=2, minutes=48)
    my_timestamps.append(later)
    later = later + datetime.timedelta(hours=2, minutes=48)
    my_timestamps.append(later)
    return (my_timestamps)


time = blood_moon("1:00")
