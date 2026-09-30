# Default value of bool() is False.

print(bool()) # Output: False
print(bool(1)) # Output: True
print(bool(0)) # Output: False

# Common errors when working with basic data types in Python include:
# - Forgetting to convert data types when necessary
# - Using the wrong data type for a particular operation
# - Not understanding how Python handles type conversion automatically

# Examples: 
# 1. Trying to add a string and an integer:
# print("Age: " + 32) # This will raise a TypeError because you cannot concatenate a string and an integer.
# 2. Forgetting to convert user input to the correct type:
user_input = input("Enter your age: ")
print("Your age is: " + user_input) # This will work, but user_input is a string, so you cannot perform arithmetic operations on it without conversion.
# age = user_input + 5 # This will raise a TypeError because user_input is a string and cannot be added to an integer without conversion.
age = int(user_input) + 5 # Correct way to handle the input by converting it to an integer first.

# Arithmetic Operations

a=10
b=5

add_result = a + b
print(add_result) # Output: 15

sub_result = a - b
print(sub_result) # Output: 5

mul_result = a * b
print(mul_result) # Output: 50

div_result = a / b
print(div_result) # Output: 2.0

floor_div_result = a // b
print(floor_div_result) # Output: 2

modulo_result = a % b
print(modulo_result) # Output: 0

exponent_result = a ** b
print(exponent_result) # Output: 100000

# Comparison Operators

print(a > b)  # Output: True
print(a < b)  # Output: False
print(a >= b) # Output: True
print(a <= b) # Output: False
print(a == b) # Output: False
print(a != b) # Output: True

# Logical Operators

# AND, NOT, OR operators are used to combine conditional statements.

# Examples of all logical operators:
x = True
y = False

print(x and y) # Output: False
print(x or y)  # Output: True
print(not x)   # Output: False
print(x ^ y) # XOR. Output: True
print(x and not y) # Output: True
print(not x or y) # Output: False
print(x | y) # OR. Output: True
print(x & y) # AND. Output: False

#Difference between and and & and or | operators:
# - The 'and' and 'or' operators are logical operators that work with boolean values
# - The '&' and '|' operators are bitwise operators that work with the binary representation of integers.

