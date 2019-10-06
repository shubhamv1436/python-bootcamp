# Difficulty Level: Beginner

# Question: Fix the program so that it outputs the surname and why the current
# program gives a KeyError

# d = {"Name": "John", "Surname": "Smith"}
# print(d["Smith"])

# Current Output
# Traceback (most recent call last):
#   File "18_key_error.py", line 19, in <module>
#     print(d["Smith"])
# KeyError: 'Smith'

# Expected Output
# Smith

# Program
d = {"Name": "John", "Surname": "Smith"}
print(d["Surname"])

# Output
# shubhamvaishnav:python-bootcamp$ python3 18_key_error.py
# Smith

# Reason: In the given problem we are trying to access the value of a key Smith
# which doesn't exist and due to which we get a KeyError, instead of that we
# should use the key "Surname" which points to the value "Smith" which is
# required by the question.
