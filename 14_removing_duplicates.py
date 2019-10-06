# Difficulty Level: Beginner

# Question: Complete the script so that it removes duplicate items from list a .
# a = ["1", 1, "1", 2]

# Expected output:
#   ['1', 2, 1]

# Hint 1: Sets are datatypes where duplicates are not allowed.
# Hint 2: You can use a set function to convert the list to a set and then a
# list function to convert the set back to a list.

# Program
from collections import OrderedDict

# Solution 1
a = ["1", 1, "1", 2]
print(list(set(a)))

# We used the set function which converts the list into set as set doesn't
# contain duplicates. Then we again convert the set to list to get our desired
# results. But the only drawback of this approach is that we loose the order
# of the items in the list

# Solution 2
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# We used OrderedDict to create a ordered dictionary of the elements present
# in the list. A dict will be created like this, [{'1':None, 1: None, 2:None}]
# Then we will convert the ordered dict to list to get the desired result

# Solution 3
a = ["1", 1, "1", 2]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
# We iterate over the list and create a new list by first checking whether the
# item exists in the other list or not, if it exists we move to next item,
# otherwise we add the item to the second list
# This is an inefficient solution as it involves two lists and the second list
# is searched for every item in the first.

# Output
# Solutions 1, 2 and 3 respectively
# shubhamvaishnav:python-bootcamp$ python3 14_removing_duplicates.py
# [1, 2, '1']
# ['1', 1, 2]
# ['1', 1, 2]
