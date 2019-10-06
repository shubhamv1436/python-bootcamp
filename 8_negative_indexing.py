# Difficulty Level: Beginner

# Question: Complete the script so that it prints out letter i  using negative
# indexing.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Expected output:
# i

# Hint: It would be silly to count from start to end since i is located closer
# to the end than to the start of the list.

# Program
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])

# Output
# shubhamvaishnav:python-bootcamp$ python3 8_negative_indexing.py
# i

# Reason: Besides the left-to-right positive indexing system that starts from
# zero, sequence data types such as lists also have a second indexing system
# that starts from -1 and decreases by one from right to left.
