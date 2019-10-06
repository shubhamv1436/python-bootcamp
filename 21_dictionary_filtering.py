# Difficulty Level: Easy

# Question: Filter the dictionary by removing all items with a value of greater
# than 1.
# d = {"a": 1, "b": 2, "c": 3}

# Expected output:
# {'a': 1}

# Hint 1: Use dictionary comprehension.
# Hint 2: Inside the dictionary comprehension access dictionary items with
# d.items()  if you are on Python 3, or dict.iteritems()  if you are on Python 2

# Program
# Solution 1
d = {"a": 1, "b": 2, "c": 3}
print({ i:j for i,j in d.items() if j <= 1})

# Solution 2
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

# Output
# shubhamvaishnav:python-bootcamp$ python3 21_dictionary_filtering.py
# {'a': 1}
