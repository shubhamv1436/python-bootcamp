# Difficulty Level: Beginner

# Question: What's wrong with the following script?

# a = 1
# _a = 2
# _a2 = 3
# 2a = 4

# Program
a = 1
_a = 2
_a2 = 3
2a = 4

# Output
# shubhamvaishnav:python-bootcamp$ python3 2_naming_rules.py
#   File "2_naming_rules.py", line 14
#     2a = 4
#      ^
# SyntaxError: invalid syntax

# Reason: Variable names can't start with numerical values
# Identifier rules:
# - A variable name can start with an alphabet
# - A variable name can start with a special character which is _(underscore)
# - A variable name can be alphanumeric but should not start with number
# - A variable name should not contain any other special character except
#   underscore

# If we remove the fourth variable assignment statement the program will execute
# successfully
