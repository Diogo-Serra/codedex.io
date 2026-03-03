#!/usr/bin/env python3
import datetime


# 2 hours and 48 minutes apart
def blood_moon(time):
    now = datetime.datetime.strptime(time, "%H:%M")
    later = now + datetime.timedelta(hours=2, minutes=48)
    print(f'[\"{later.strftime("%H:%M")}\",', end=" ")
    later += datetime.timedelta(hours=2, minutes=48)
    print(f'\"{later.strftime("%H:%M")}\",', end=" ")
    later += datetime.timedelta(hours=2, minutes=48)
    print(f'\"{later.strftime("%H:%M")}\"]')


blood_moon("10:32")
