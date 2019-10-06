# Difficulty Level: Beginner

# Question: Complete the script so it generates the expected output using
# my_range  as input data. Please note that the items of the expected list
# output are all strings.
# my_range = range(1, 21)

#  Expected output:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

# Hint: Use the map  function.

# Program
# Solution 1
my_range = range(1, 21)
print([str(i) for i in my_range])

# Solution 2
my_range = range(1, 21)
print(list(map(str, my_range)))

# Output
# shubhamvaishnav:python-bootcamp$ python3 13_ranges_of_strings.py
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
