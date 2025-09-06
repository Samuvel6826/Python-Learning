# Question:
# Write an example for different Python data types such as 
# Number (Integer, Float, Complex), String, Boolean, List, Tuple, Set, and Dictionary.

# Numbers
integer_num = 10                     # Integer
float_num = 9.8                      # Float
complex_num = 4 - 4j                 # Complex number

# String
name = "Sam"

# Boolean
is_student = True

# List (ordered, changeable, allows duplicates)
fruits = ["apple", "banana", "cherry"]

# Tuple (ordered, unchangeable, allows duplicates)
coordinates = (10.5, 20.3)

# Set (unordered, no duplicates)
unique_numbers = {1, 2, 3, 3, 2}

# Dictionary (key-value pairs)
person = {
    "name": "Sam",
    "age": 22,
    "country": "India"
}

# Printing all with type
print(integer_num, "=>", type(integer_num))
print(float_num, "=>", type(float_num))
print(complex_num, "=>", type(complex_num))
print(name, "=>", type(name))
print(is_student, "=>", type(is_student))
print(fruits, "=>", type(fruits))
print(coordinates, "=>", type(coordinates))
print(unique_numbers, "=>", type(unique_numbers))
print(person, "=>", type(person))