# For loop

# range(5)  # Generates numbers from 0 to 4

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

for i in range(1, 6):  # Generates numbers from 1 to 5
    print(i)  # Output: 1, 2, 3, 4, 5

for i in range(1, 10, 2):  # Generates odd numbers from 1 to 9. 
    print(i)  # Output: 1, 3, 5, 7, 9    
# The third parameter is the step, which determines the increment between each number in the sequence.

for i in range(10, 0, -1):  # Generates numbers from 10 to 1 in reverse order
    print(i)  # Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# The third parameter is negative, which means the sequence will decrement.

## Strings
string = "Hello, World!"
for char in string:
    print(char)  # Output: H, e, l, l, o, ,,  , W, o, r, l, d, !

## while loop
# The while loop continues to execute a block of code as long as a specified condition is true.
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1  # Increment count by 1

# break statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
# Example:
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is equal to 5
    print(i)  # Output: 0, 1, 2, 3, 4

# continue statement
# The continue statement is used to skip the current iteration of a loop and move on to the next iteration.
# Example:
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)  # Output: 1, 3, 5, 7, 9

# Nested loops
# Nested loops are loops within loops. The inner loop is executed completely for each iteration of the outer loop.
# Example:
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i: {i}, j: {j}")  # Output: i: 0, j: 0; i: 0, j: 1; i: 1, j: 0; i: 1, j: 1; i: 2, j: 0; i: 2, j: 1    

# What does the f in f"i: {i}, j: {j}" mean?
# The f in f"i: {i}, j: {j}" indicates that this is an f-string, which is a way to format strings in Python. 
# It allows you to embed expressions inside string literals, using curly braces {}. 
# The expressions are evaluated at runtime and formatted using the __str__() method of the object. 
# In this case, the values of i and j are inserted into the string at the specified locations.        