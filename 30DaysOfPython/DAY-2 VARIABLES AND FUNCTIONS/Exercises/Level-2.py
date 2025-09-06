# Variables from before
first_name = "Sam"
last_name = "A"
full_name = first_name + " " + last_name
country = "India"
city = "Nagercoil"
age = 22
year = 2025
is_married = False
is_true = True
is_light_on = True
a, b, c = 10, 20, 30

# 1. Check the data type of all your variables using type()
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

# 2. Using the len() built-in function, find the length of your first name
print("Length of first name:", len(first_name))

# 3. Compare the length of your first name and your last name
print("Is first name longer than last name?", len(first_name) > len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 5. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# Printing results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# 12. The radius of a circle is 30 meters.
import math

radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

# Take radius as user input and calculate the area
user_radius = float(input("Enter radius of a circle: "))
user_area = math.pi * user_radius ** 2
print("Area of circle with radius", user_radius, "is:", user_area)

# 13. Get first name, last name, country and age from a user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# 14. Show Python keywords
help('keywords')