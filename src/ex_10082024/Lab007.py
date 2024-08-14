# Rules about Variables

'''
1. They start with a letter (A-Z, a-z)
2. an underscore followed by zero or more letters
3. underscores, and digits (0-9)
4. Age and age are two different identifiers because Python is "case-sensitive"
5. Should not start with number
6. No special characters are allowed.
'''

age = 24
Age = 23
print(age)
# 24
print(Age)
# 23

_ = 55
print(_)
# 55

_ = _+1
print(_)
# 56

# 1bc = 1234
# Error - SyntaxError: invalid decimal literal

abc123 = 234
print(abc123)
# 234

long_variable_name_created = "Hello"
print(long_variable_name_created)
# valid variable name

_naruto = "Uzumaki"
print(_naruto)
# Uzumaki

# $123 = 23
# SyntaxError: invalid syntax

# $abc = 245
# SyntaxError: invalid syntax

# abc$123 = "Itachi"
# SyntaxError: invalid syntax