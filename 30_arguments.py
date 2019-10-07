# Difficulty Level: Beginner

# Question:  Why do you get an error and how would you fix it?

# def foo(a=2, b):
#     return a + b
# print(foo(1))

# Hint: Always put non default parameters first followed by default ones.

# Current Output
# shubhamvaishnav:python-bootcamp$ python3 30_arguments.py
#   File "30_arguments.py", line 5
#     def foo(a=2, b):
#            ^
# SyntaxError: non-default argument follows default argument

# Expected Output

# Program
def foo(b, a=2):
    return a + b

print(foo(1))

# Output
# shubhamvaishnav:python-bootcamp$ python3 30_arguments.py
# 3

# Reason: Non default parameters are always specified before the default ones.
