# Difficulty Level: Beginner

# Question: Fix the last line so that it outputs the sum of 1 and 2.

# a = "1"
# b = 2
# print(a + b)

# Output
# shubhamvaishnav:python-bootcamp$ python3 4_type_error.py
# Traceback (most recent call last):
#   File "4_type_error.py", line 21, in <module>
#     print(a + b)
# TypeError: can only concatenate str (not "int") to str

# Expected output:
# 3

# Hint: str(1)  converts integer 1 to string "1". What would convert string
# "1" to integer 1?

# Program
a = "1"
b = 2
print(int(a) + b)

# Output
# shubhamvaishnav:python-bootcamp$ python3 4_type_error.py
# 3
