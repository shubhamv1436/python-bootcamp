# Difficulty Level: Beginner

# Question: Executing the code will throw an error. Can you explain why?

# a = 1
# b = 2
# print(a == b)
# print(b == c)

# Program
a = 1
b = 2
print(a == b)
print(b == c)

# Output
# shubhamvaishnav:python-bootcamp$ python3 3_comapre_vs_assign.py
# False
# Traceback (most recent call last):
#   File "3_comapre_vs_assign.py", line 14, in <module>
#     print(b == c)
# NameError: name 'c' is not defined

# Reason: Variable named c is not defined which is used to compare with the
# value of variable b
# If we define a variable c like `c = 3` the program will execute successfully
