# bounce.py
#
# Exercise 1.5

height = 100 # meters
bounce = 1
const = 0.6

while bounce < 11:
    height = round(height * const, 4)
    bounce = bounce + 1
    print (bounce, height)
