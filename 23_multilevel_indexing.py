# Difficulty Level: Easy

# Question: Access the third value of key b  from the dictionary.
# from pprint import pprint
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# Expected output:
# 13

# Hint: You need square brackets after square brackets here.

# Program
d = dict(a = list(range(1, 11)),
 b = list(range(11, 21)),
 c = list(range(21, 31)))

print(d["b"][2])

# Output
# shubhamvaishnav:python-bootcamp$ python3 23_multilevel_indexing.py
# 13
