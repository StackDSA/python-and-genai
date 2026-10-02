# Dictionaries are used to store data values in key:value pairs.
# They are mutable, unordered, changeable, and do not allow duplicates i.e., keys must be unique.

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,  
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(my_dict))  # Output: <class 'dict'>

empty_dict = {}
print(empty_dict)  # Output: {}

# Or we can create a dictionary using the dict() constructor
my_dict = dict(name="John", age=30, city="New York")
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

empty_dict = dict()
print(empty_dict)  # Output: {}

# Accessing elements in a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Accessing elements using the get() method
print(my_dict.get("name"))  # Output: John  

# Accessing a non-existing key using get() returns None instead of raising an error
print(my_dict.get("country"))  # Output: None

# Modifying elements in a dictionary
my_dict["age"] = 31  # Update the value of the key "age"
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding new elements to a dictionary
my_dict["country"] = "USA"  # Add a new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing elements from a dictionary
del my_dict["city"]  # Remove the key "city" and its value
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Using pop() method to remove an item
age = my_dict.pop("age")  # Remove the key "age" and return its value
print(age)  # Output: 31
print(my_dict)  # Output: {'name': 'John', 'country': 'USA'}

# Methods to get keys, values, and items
print(my_dict.keys())    # Output: dict_keys(['name', 'country'])
print(my_dict.values())  # Output: dict_values(['John', 'USA'])
print(my_dict.items())   # Output: dict_items([('name', 'John'), ('country', 'USA')])
print(list(my_dict.keys()))    # Output: ['name', 'country']
print(list(my_dict.values()))  # Output: ['John', 'USA']
print(list(my_dict.items()))   # Output: [('name', 'John'), ('country', 'USA')]
print(len(my_dict))  # Output: 2
print(tuple(my_dict.items()))  # Output: (('name', 'John'), ('country', 'USA'))
print(tuple(my_dict.keys()))  # Output: ('name', 'country')
print(tuple(my_dict.values()))  # Output: ('John', 'USA')

# Shallow copy of a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'John', 'country': 'USA'}
my_dict_copy["name"] = "Jane"  # Modify the copy
print(my_dict_copy)  # Output: {'name': 'Jane', 'country': 'USA'}
print(my_dict)  # Output: {'name': 'John', 'country': 'USA'}

# Iterating through a dictionary
for key in my_dict:
    print(key, my_dict[key])  # Output: name John \n country USA

# Iterate through key value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name John \n country USA

# Nested dictionaries
nested_dict = { 
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Jane", "age": 25}
}

print(nested_dict)  # Output: {'person1': {'name': 'John', 'age': 30}, 'person2': {'name': 'Jane', 'age': 25}}
print(nested_dict["person1"]["name"])  # Output: John
print(nested_dict["person2"]["age"])   # Output: 25

# Iterating through a nested dictionary
for person, details in nested_dict.items():
    print(person, details)  # Output: person1 {'name': 'John', 'age': 30} \n person2 {'name': 'Jane', 'age': 25}
    for key, value in details.items():
        print(key, value)  # Output: name John \n age 30 \n name Jane \n age 25

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Conditional Dictionary Comprehension
even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squared_dict)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

## Practical examples

# Counting the frequency of elements in a list using a dictionary
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_dict = {}

for item in my_list:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

print(frequency_dict)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

# Merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}  # dict2 values will overwrite dict1 values for duplicate keys
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}