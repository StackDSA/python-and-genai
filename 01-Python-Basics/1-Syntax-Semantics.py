## this is a single line comment

''' 
    this is a multi-line comment 
'''

## Python is a case sensitive language, so the following two variables are different
a = 10  
A = 20

print(a)  # prints 10
print(A)  # prints 20

''' Indentation in Python is very important as it defines the blocks of code. 
Commonly, four spaces are used for indentation.   
For example, in a function or a loop, the code that belongs to that block must be indented.
''' 

age=10
if age>18:
    print("You are an adult. " + str(age))  # This line is indented and belongs to the if block
else:
    print("You are not an adult. " + str(age))  # This line is indented and belongs to the else block

# Multiple statements can be written on a single line using a semicolon (;) to separate them. 
# For example:
x = 5; y = 10; z = 15

print(x, y, z)

# Variable assignment
age = 25  # Assigning an integer value to the variable 'age'
name = "John"  # Assigning a string value to the variable 'name'

print(type(age))  # This will return <class 'int'>
print(type(name))  # This will return <class 'str'>