# Difficulty Level: Easy

# Question: Make a script to print out letters of English alphabet from a to z

# Program
# Solution 1
import string

for letter in string.ascii_lowercase:
    print(letter, end=" ")

# string  is a built-in module and string.ascii_lowercase returns a string
# object containing all 26 letters of English alphabet.
# Then we simply iterate through that string and print out the string items.

# Solution 2
print(*list(map(chr,range(97,123))))

# We use the ascii values of lower case alphabets and apply chr function to each
# value of the list to convert them into charaters.
# Then create a list form them and print out the string items.

# Output
# shubhamvaishnav:python-bootcamp$ python3 25_print_alphabet.py
# a b c d e f g h i j k l m n o p q r s t u v w x y z
