# tuples are ordered collections of items that are immutable (cannot be changed after creation). 
# They are defined using parentheses ().
# Can have elements of different data types.

empty_tuple = ()
print(empty_tuple)  # Output: ()
print(type(empty_tuple))  # Output: <class 'tuple'>

#Converting a list to a tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Converting tuple to a list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4, 5]


# Accessing elements in a tuple
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
print(my_tuple[-1])  # Output: 50
print(my_tuple[1:4])  # Output: (20, 30, 40)
print(my_tuple[::-1])  # Output: (50, 40, 30, 20, 10) - Reversing the tuple

#Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Copying a tuple
original_tuple = (1, 2, 3)
copied_tuple = original_tuple
print(copied_tuple)  # Output: (1, 2, 3)

# Unpacking a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Repeating elements in a tuple
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Immutable nature of tuples
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError since tuples are immutable

# Tuple methods
my_tuple = (1, 2, 3, 2, 1)
print(my_tuple.count(2))  # Output: 2 (counts occurrences of 2)
print(my_tuple.index(3))  # Output: 2 (returns the index of the first occurrence of 3)
print(len(my_tuple))  # Output: 5 (returns the number of elements in the tuple)

# Packing and unpacking tuples
packed_tuple = 1, 2, 3  # Packing
print(packed_tuple)  # Output: (1, 2, 3)
a, b, c = packed_tuple  # Unpacking
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

unpacked_tuple = (4, 5, 6, 7, 8, 9)
x, *y, z = unpacked_tuple  # Unpacking   
print(x)  # Output: 4
print(y)  # Output: [5, 6, 7, 8] Middle elements as a list
print(z)  # Output: 9    

# Nested tuples and slicing in them 
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[0][0])  # Output: 1
print(nested_tuple[1:])  # Output: ((3, 4), (5, 6)) (slicing)

# Iterating over a nested tuple
for item in nested_tuple:
    print(item)  # Output: (1, 2) (3, 4) (5, 6) (each tuple on a new line)
