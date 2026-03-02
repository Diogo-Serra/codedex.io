#!/usr/bin/env python3


height = int(input("Your height: "))
credits = int(input("Your credits: "))
if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif credits < 10:
  print("You don't have enough credits.")
elif height < 137:
  print("You are not tall enough")
else:
  print("Requirements not met")
