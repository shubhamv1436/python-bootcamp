# Difficulty Level: Easy

# Question:  Please write a function that calculates liquid volume in a sphere
# using the following formula.

# Liquid volume = (4 * pi * r^3)/3 - (pi * h^2 * (3*r - h) )/3

# The radius r  is always 10, so consider making it a default parameter.

# You can then test your solution by passing 2 for h and you should get the
# expected output.

# Expected output:
# 4071.5040790523717

# Program
import math

def calculate_liquid_volume(h,r=10):
    liquid_volume = (4 * math.pi * r**3)/3 - (math.pi * h**2 * (3*r - h) )/3
    return liquid_volume

print(calculate_liquid_volume(2))

# Output
# shubhamvaishnav:python-bootcamp$ python3 29_liquid_volume_calculator.py 
# 4071.5040790523717
