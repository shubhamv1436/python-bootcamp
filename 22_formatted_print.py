# Difficulty Level: Easy

# Create a dictionary of keys a, b and c where each key is a list from 1 to 10,
# 11 to 20 and 21 to 30 respectively and print out the dictionary

# Expected Output
# {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#  'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

# Program
from pprint import pprint
d = dict(a= list(range(1,11)),
b = list(range(11,21)),
c = list(range(21,31)))
pprint(d)

# Output
# shubhamvaishnav:python-bootcamp$ python3 22_formatted_print.py
# {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#  'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

# pprint is used for pretty print
