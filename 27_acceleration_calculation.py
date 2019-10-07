# Difficulty Level: Beginner

# Question: Create a function that calculates acceleration given initial
# velocity v1, final velocity v2, start time t1, and end time t2.
# The formula for acceleration is:
# a = (v2-v1)/(t2-t1)

# To test your solution, call the function by inputting values 0, 10, 0, 20
# for v1, v2, t1, and t2 respectively, and you should get the expected output.

# Expected output:
# 0.5

# Hint 1: Your function definition should have four parameters.
# Hint 2: The acceleration formula inside the function would look like
# a = (v2 - v1) / (t2 - t1) .

# Program
def calculate_acceleration(v1,v2,t1,t2):
    a = (v2 - v1) / (t2 - t1)
    print(a)

calculate_acceleration(0,10,0,20)

# Output
# shubhamvaishnav:python-bootcamp$ python3 27_acceleration_calculation.py 
# 0.5
