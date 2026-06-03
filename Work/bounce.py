# bounce.py
#
# Exercise 1.5
# Rubber ball dropped from 100 m.
# Each time it hits the ground, it bounces back up to 3/5 the height it fell.
# Print a table showing the height of the first 10 bounces.

rebound_percentage = 0.6
height = 100
bounce = 1

while bounce <= 10:
    height = height * rebound_percentage
    print(bounce, round(height,4))
    bounce = bounce + 1