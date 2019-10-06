# Difficulty Level: Easy

# Question: Calculate the sum of all dictionary values.
# d = {"a": 1, "b": 2, "c": 3}

# Expected output:
#  6

# Program
# Solution 1
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))

# Solution 2
d = {"a": 1, "b": 2, "c": 3}
total = 0
for i in d.values():
    total += i
print(total)

# Output
# shubhamvaishnav:python-bootcamp$ python3 20_apply_functions_to_dictionary_items.py
# 6
