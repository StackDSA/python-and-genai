# Lists are ordered, mutable collections of items.
# They can contain items of different data types.


lst = []
print(lst)  # Output: []

# Creating a list with initial values
numbers = [1, "two", 3.0, True]
print(numbers)  # Output: [1, 'two', 3.0, True]

# Accessing elements in a list
print(numbers[0])  # Output: 1
print(numbers[1])  # Output: 'two'
print(numbers[2])  # Output: 3.0
print(numbers[3])  # Output: True
print(numbers[-1])  # Output: True (last element)
print(numbers[1:3])  # Output: ['two', 3.0] (slicing)
print(numbers[:2])  # Output: [1, 'two'] (first two elements)
print(numbers[2:])  # Output: [3.0, True] (from index 2 to last)

# Modifying elements in a list
numbers[1] = "three"
print(numbers)  # Output: [1, 'three', 3.0, True]

# Adding elements to a list
numbers.append("new item")
print(numbers)  # Output: [1, 'three', 3.0, True, 'new item']

# Inserting elements at a specific index
numbers.insert(2, "inserted item")
print(numbers)  # Output: [1, 'three', 'inserted item', 3.0, True, 'new item']

# Removing elements from a list
numbers.remove("three")
print(numbers)  # Output: [1, 'inserted item', 3.0, True, 'new item']

# Popping elements from a list
popped_item = numbers.pop()  # Removes and returns the last item
print(popped_item)  # Output: 'new item'
print(numbers)  # Output: [1, 'inserted item', 3.0, True]

# Fun fact

some_array = [1, 2, 3, 4, 5]
some_array[1:3] = "replaced"
print(some_array)  # Output: [1, 'r', 'e', 'p', 'l', 'a', 'c', 'e', 'd', 4, 5]

# Remove all elements from a list
some_array.clear()

# Slicing Lists:

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[2:])  # Output: [3, 4, 5]
print(numbers[::2])  # Output: [1, 3, 5] (every second element) (Last parameter is the step size)
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1] (reverse order)


#Concatenation of lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

#Copying a list
original_list = [1, 2, 3]
new_list = original_list.copy()
print(new_list)  # Output: [1, 2, 3]

# Iterating over a list
for num in numbers:
    print(num)  # Output: 1 2 3 4 5 (each number on a new line)

# To iterate over a list with index, we can use the enumerate() function
for index, num in enumerate(numbers):
    print(f"Index: {index}, Value: {num}") 
    # The f stands for formatted string literals, which allows us to embed expressions inside string literals using curly braces {}.
    # Output:
    # Index: 0, Value: 1
    # Index: 1, Value: 2
    # Index: 2, Value: 3
    # Index: 3, Value: 4
    # Index: 4, Value: 5    

# List comprehensions provide a concise way to create lists.
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Another example of list comprehension using for loop and if condition
lst = [x for x in range(10) if x % 2 == 0]
print(lst)  # Output: [0, 2, 4, 6, 8]

# nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Or using nested loops
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)

print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Or combining 2 lists using list comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [x + y for x in list1 for y in list2]
print("Combined is:", combined)  # Output: [5, 6, 7, 6, 7, 8, 7, 8, 9]