# Difficulty Level: Beginner

# Question:  Why is there an error in the code and how would you fix it?
#
# def foo(a, b):
#     print(a + b)
#
# x = foo(2, 3) * 10
#
# Hint: This function needs to return something to be complete.

# Current Output
# shubhamvaishnav:python-bootcamp$ python3 28_type_error.py
# 5
# Traceback (most recent call last):
#   File "28_type_error.py", line 8, in <module>
#     x = foo(2, 3) * 10
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Expected Output
# 50

# Program
def foo(a, b):
    return a + b

x = foo(2, 3) * 10
print(x)

# Output
# shubhamvaishnav:python-bootcamp$ python3 28_type_error.py
# 50

# Reason: As the function return nothing, the expression used to initialize
# x results in a TypeError as we try to add a value of NoneType to an integer.
