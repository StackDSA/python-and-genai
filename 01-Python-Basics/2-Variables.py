age=32
height=1.75
name="John Doe"
is_student=True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student?:", is_student)

# Variable names must start with a letter or an underscore (_) and can contain letters, numbers, and underscores. 
# They are case-sensitive, meaning that 'age' and 'Age' would be considered different variables.

#Invalid variable names examples:
# 1name = 25  # Starts with a number
# my-name = "John"  # Contains a hyphen
# class = "Math"  # 'class' is a reserved keyword in Python

# Variable types in Python:
# 1. Integer (int): Whole numbers, e.g., 1, 42, -
# 2. Float (float): Decimal numbers, e.g., 3.14, -0.001
# 3. String (str): Text, e.g., "Hello", 'Python'
# 4. Boolean (bool): True or False values, e.g., True, False


# Type conversion examples:
# Converting integer to float
age = 32
height = float(age)  # Converts age to float
print("Height as float:", height) #Output: Height as float: 32.0

# Dynamic typing in Python allows you to change the type of a variable by assigning a new value of a different type.
# For example:
age = 32  # Initially an integer
age = "Thirty-two"  # Now a string

# Input from users can be taken using the input() function, which always returns a string. 
# You may need to convert it to the appropriate type if necessary.
# Example: 
user_input = input("Enter your age: ")
age = int(user_input)  # Converts the string to an integer
print("Your age is:", age)

