#!/usr/bin/env python3
import datetime


# 2 hours and 48 minutes apart
def blood_moon(time):
    now = datetime.datetime.strptime(time, "%H:%M")
    my_timestamps = []
    my_timestamps.append(now + datetime.timedelta(hours=2, minutes=48))
    my_timestamps.append(datetime.timedelta(hours=2, minutes=48))
    my_timestamps.append(datetime.timedelta(hours=2, minutes=48))
    for time in my_timestamps:
        print(time)
