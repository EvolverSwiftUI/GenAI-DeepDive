# resource link a YouTube video by Beau Carnes
# https://youtu.be/PNSIWjWAA7o?si=Trefoh8BwlqB_WTy



# basic math
# 2 + 3 * 8 = 26
print("2 + 3 * 8 =", 2 + 3 * 8)

# string concatenation
first_name = "Sivaram"
last_name = "Yadav"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

name = "sivaram"*5
print("Name repeated 5 times:", name)

# create a variable
spam = "hello"
print(spam)

# take input from user
user_name = input("Enter your name: ")
print("Hello ", user_name)

# print with formatting
print("Hi, How are you, {}".format(user_name))

# print with formatting with string interpolation
print(f"Welcome, {user_name}!")

# length of a string
length = len(full_name)
print("Length of full name:", length)

# primitive datatypes 
# int
# str
# float
# bool

# In python everything is a class / object.

# type conversion
num_str = "123"
num_int = int(num_str)
print("Converted string to int:", num_int)
num_float = float(num_str)
print("Converted string to float:", num_float)
num_str_back = str(num_int)
print("Converted int back to string:", num_str_back)

# check type
print("Type of num_str_back:", type(num_str_back))

# conditional operations
# ==, !=, >, <, >=, <=
a = 10
b = 20
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# for booleans to compare in python use 'is' and 'is not' operators
print(True is True)
print(False is not True)

# logical operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)
a = 5
b = 10
print("a > 0 and b < 20:", a > 0 and b < 20)
print("a < 0 or b < 20:", a < 0 or b < 20)  

# we can use combination of multiple and and not operators
print("a > 0 and not (b < 5):", a > 0 and not (b < 5))  

# if statement
num = 15
if num > 10:
    print("Number is greater than 10")
elif num == 10:
    print("Number is equal to 10")
else:
    print("Number is less than 10")

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# while with break
num = 0
while True:
    if num >= 3:
        break
    print("Number in while loop with break:", num)
    num += 1
print("Exited the while loop")

# in python indentation is very important

# while loop with continue and break
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    try:
        number = int(user_input)
        if number < 0:
            print("Negative number entered, skipping...")
            continue
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input, please enter a valid number.")


# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# for loop with range
for i in range(5):
    print("Number from range:", i)

# for loop with break
for i in range(10):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("i in for loop with break:", i)

# for loop with continue
for i in range(10):
    if i % 2 == 0:
        print("Skipping even number i =", i)
        continue
    print("i in for loop with continue:", i)


# for loop with range and step
for i in range(0, 10, 2):
    print("Number from range with step 2:", i)  

# for loop counting down
for i in range(10, -1, -1):
    print("Countdown:", i)

# for loop with if-else
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# importing module
import random
for i in range(5):
    print("Random number between 1 and 100:", random.randint(1, 100))

#  import everything from a module
from random import *
for i in range(5):
    print("Random float between 0 and 1:", random())

# import specific function from a module
from random import choice
colors = ["red", "blue", "green", "yellow"]
for i in range(5):
    print("Random color from list:", choice(colors))
    # output will be different each time

# exiting the program
import sys
print("Exiting the program now.")
sys.exit()

# exit with while loop
import sys
while True:
    user_input = input("Type 'exit' to quit the program: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        sys.exit()
    else:
        print("You entered:", user_input)

# functions
def greet(name):
    print("Hello, {}".format(name))

# call the function
greet("Sivaram")

# function with return value
def add(a, b):
    return a + b

result = add(5, 10)
print("Sum of 5 and 10 is:", result)

# function with default parameter
def power(base, exponent=2):
    return base ** exponent 

power_result = power(3)
print("3 raised to the power of 2 is:", power_result)

# function with multiple parameters
def multiply(a, b, c):
    return a * b * c

multiply_result = multiply(2, 3, 4)
print("Multiplication of 2, 3 and 4 is:", multiply_result)

# function with keyword arguments
def introduce(name, age):
    print("My name is {} and I am {} years old.".format(name, age))
introduce(age=25, name="Sivaram")
# function with variable number of arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
sum_result = sum_all(1, 2, 3, 4, 5)
print("Sum of all numbers is:", sum_result)

# global vs local variables
x = 10  # global variable
def modify_global():
    global x
    x = 20  # modifying global variable
    print("Inside function, modified global x to:", x)
modify_global()
print("Outside function, global x is:", x)

# try-except for error handling
try:
    num = int(input("Enter a number to divide 100: "))
    result = 100 / num
    print("Result of division is:", result)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero! : {}".format(e))
except ValueError as e:
    print("Error: Invalid input, please enter a valid number! : {}".format(e))
except Exception as e:
    print("An unexpected error occurred:", e)

# finally block
try:
    num = int(input("Enter a number to divide 50: "))
    result = 50 / num
    print("Result of division is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, please enter a valid number!")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution of try-except block is complete.")


# ======== LIST ===========

# list creation and manipulation
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)
# add element
fruits.append("date")
print("Fruits list after appending date:", fruits)
# remove element
fruits.remove("banana")
print("Fruits list after removing banana:", fruits)
# insert at specific index
fruits.insert(1, "blueberry")
print("Fruits list after inserting blueberry at index 1:", fruits)
# pop element
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits list after popping an element:", fruits)
# count elements
print("Number of fruits in the list:", len(fruits))
# access elements
print("First fruit in the list:", fruits[0])
print("Last fruit in the list:", fruits[-1])
# sort list
fruits.sort()
print("Sorted fruits list:", fruits)  
# reverse list  
fruits.reverse()
print("Reversed fruits list:", fruits)
# looping through a list
for fruit in fruits:
    print("Fruit from loop:", fruit)
# list comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared numbers from 1 to 5 using list comprehension:", squared_numbers)
# sublist
sublist = fruits[1:3]
print("Sublist of fruits from index 1 to 2:", sublist)  
# list slicing
sliced_list = fruits[:2]
print("Sliced list of first two fruits:", sliced_list)  
# list concatenation
more_fruits = ["elderberry", "fig"]
all_fruits = fruits + more_fruits
print("All fruits after concatenation:", all_fruits)
# list repetition
repeated_fruits = fruits * 2
print("Fruits list repeated twice:", repeated_fruits)
# check membership
print("Is 'apple' in fruits list?", "apple" in fruits)
print("Is 'banana' not in fruits list?", "banana" not in fruits)
# slicing using negative step indexing
reversed_fruits = fruits[::-1]
print("Reversed fruits list using slicing:", reversed_fruits)
# reverse slicing sublist
reverse_sublist = fruits[-4:-1]
print("Reverse sublist of fruits from index -4 to -2:", reverse_sublist)
# copying a list
copied_fruits = fruits.copy()
print("Copied fruits list:", copied_fruits)
# copy list using slicing
sliced_copied_fruits = fruits[:]
print("Sliced copied fruits list:", sliced_copied_fruits)
#  length of a list
print("Length of fruits list:", len(fruits))
# clearing a list
fruits.clear()
print("Fruits list after clearing:", fruits)
# delete at 2nd index
numbers = [10, 20, 30, 40, 50]
del numbers[2]
print("Numbers list after deleting element at index 2:", numbers)
# find index of an element
index_of_40 = numbers.index(40)
print("Index of 40 in numbers list:", index_of_40)
# count occurrences of an element
numbers.append(20)
count_of_20 = numbers.count(20)
print("Count of 20 in numbers list:", count_of_20)
# enumerate a list
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")    
# zip two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped list of list1 and list2:", zipped) 
# for with zip of lists
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")
# destructuring a list
numbers_list = [100, 200, 300]
a, b, c = numbers_list
print("Destructured values from numbers_list:", a, b, c)
# swapping values using destructuring
x = 5
y = 10
print("Before swapping: x =", x, ", y =", y)
x, y = y, x
print("After swapping: x =", x, ", y =", y)
# nested list   
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
print("Element at row 1, column 2 of nested list:", nested_list[1][2])  


# ======== TUPLES ===========

# tuple creation and manipulation
coordinates = (10, 20)
print("Coordinates tuple:", coordinates)
# access elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])
# tuple unpacking
x, y = coordinates
print("Unpacked coordinates: x =", x, ", y =", y)
# length of a tuple
print("Length of coordinates tuple:", len(coordinates))
# looping through a tuple
for coord in coordinates:
    print("Coordinate from tuple:", coord)
# tuple concatenation
more_coords = (30, 40)
all_coords = coordinates + more_coords
print("All coordinates after concatenation:", all_coords)
# tuple repetition
repeated_coords = coordinates * 2
print("Coordinates tuple repeated twice:", repeated_coords)
# check membership  
print("Is 10 in coordinates tuple?", 10 in coordinates)
print("Is 50 not in coordinates tuple?", 50 not in coordinates)
# nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Element at index 1,1 of nested tuple:", nested_tuple[1][1])  
# tuple with single element
single_element_tuple = (100,)
print("Single element tuple:", single_element_tuple)
# destructuring a tuple
point = (7, 14)
a, b = point    
print("Destructured values from point tuple:", a, b)
# slicing a tuple   
numbers_tuple = (10, 20, 30, 40, 50)
sliced_tuple = numbers_tuple[1:4]
print("Sliced tuple from index 1 to 3:", sliced_tuple)
# list to tuple conversion
num_list = [1, 2, 3, 4, 5]
num_tuple = tuple(num_list)
print("Converted tuple from list:", num_tuple)
# tuple to list conversion
converted_list = list(num_tuple)
print("Converted list from tuple:", converted_list)



# ======== DICTIONARY ===========

# dictionary creation and manipulation
person = {"name": "Sivaram", "age": 30, "city": "New York"}
print("Person dictionary:", person)
# access value
name = person["name"]
print("Name from person dictionary:", name)
# add key-value pair
person["country"] = "USA"
print("Person dictionary after adding country:", person)
# update value
person["age"] = 31
print("Person dictionary after updating age:", person)
# delete key-value pair
del person["city"]
print("Person dictionary after deleting city:", person)
# access keys and values
print("Keys in person dictionary:", person.keys())
print("Values in person dictionary:", person.values())
# access dictionary items
print("Items in person dictionary:", person.items())
# looping through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
# dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print("Squared dictionary from 1 to 5 using dictionary comprehension:", squared_dict)
# check membership
print("Is 'name' a key in person dictionary?", "name" in person)
print("Is 'city' not a key in person dictionary?", "city" not in person)
# check value membership
print("Is 'USA' a value in person dictionary?", "USA" in person.values())
print("Is 'Canada' not a value in person dictionary?", "Canada" not in person.values())
# check key existence before accessing
if "age" in person.keys():
    print("Age exists in person dictionary:", person["age"])
else:
    print("Age key does not exist in person dictionary.")
# get method to access value
age = person.get("age", "Not Found")
print("Age from person dictionary using get method:", age)
# set default value for a key
person.setdefault("profession", "Engineer")
print("Person dictionary after setting default profession:", person)
# clear dictionary
person.clear()
print("Person dictionary after clearing:", person)  
# delete dictionary
del person
print("Person dictionary deleted.")
# Note: Accessing 'person' after deletion will raise an error
# print(person)  # Uncommenting this line will raise a NameError

# merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary of dict1 and dict2:", merged_dict)

# ======= SET ========
# set creation and manipulation
my_set = {1, 2, 3, 4, 5}
print("My set:", my_set)
# set creation using set() function
another_set = set([4, 5, 6, 7, 8])
print("Another set created using set() function:", another_set)
# add element
my_set.add(6)
print("My set after adding 6:", my_set)
# remove element
my_set.remove(3)
print("My set after removing 3:", my_set)
# discard element (no error if not found)
my_set.discard(10)
print("My set after discarding 10 (not present):", my_set)
# pop element
popped_element = my_set.pop()
print("Popped element from my set:", popped_element)
print("My set after popping an element:", my_set)
# clear set
my_set.clear()
print("My set after clearing:", my_set)
# set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# union
set_union = set_a | set_b
print("Union of set_a and set_b:", set_union)
# intersection
set_intersection = set_a & set_b
print("Intersection of set_a and set_b:", set_intersection)
# difference
set_difference = set_a - set_b
print("Difference of set_a and set_b (set_a - set_b):", set_difference)
# symmetric difference
set_sym_diff = set_a ^ set_b
print("Symmetric difference of set_a and set_b:", set_sym_diff)
# check membership  
print("Is 2 in set_a?", 2 in set_a)
print("Is 5 not in set_a?", 5 not in set_a)
# looping through a set
for element in set_b:
    print("Element from set_b:", element)
# set comprehension
squared_set = {x**2 for x in range(1, 6)}
print("Squared set from 1 to 5 using set comprehension:", squared_set)
# length of a set
print("Length of set_b:", len(set_b))
# frozen set (immutable set)
frozen = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen)
# set methods
set_c = {1, 2, 3}
set_d = {3, 4, 5}
# isdisjoint
print("Are set_c and set_d disjoint?", set_c.isdisjoint(set_d))
# issubset
print("Is set_c a subset of set_d?", set_c.issubset(set_d))
# issuperset
print("Is set_d a superset of set_c?", set_d.issuperset(set_c)) 
# copy set
set_e = set_c.copy()
print("Copied set_e from set_c:", set_e)
# update set
set_c.update({4, 5})
print("set_c after updating with {4, 5}:", set_c)   
# intersection update
set_c.intersection_update({2, 3, 4})
print("set_c after intersection update with {2, 3, 4}:", set_c)   
# difference update
set_c.difference_update({3})
print("set_c after difference update with {3}:", set_c)   
# symmetric difference update
set_c.symmetric_difference_update({1, 4})
print("set_c after symmetric difference update with {1, 4}:", set_c)    

# escape characters in strings
print("He said, \"Hello!\"") # double quotes
print('It\'s a beautiful day!') # single quote
print("This is a backslash: \\") # backslash 
print("First Line\nSecond Line") # new line
print("Column1\tColumn2\tColumn3") # tab space
print("This is a bell sound\a") # bell/alert
print("This is a backspace\b example.") # backspace
print("This is a form feed\f example.") # form feed
print("This is a carriage return example.\rOverwritten") # carriage return
print("This is a vertical tab\v example.") # vertical tab
print("Unicode character: \u03A9") # Greek capital letter Omega
print("Hexadecimal character: \x48") # Character 'H' in hexadecimal 
print("Octal character: \101") # Character 'A' in octal
print(r"This is a raw string with \n no escape processing.") # raw string
# multi-line string
multi_line = """This is a multi-line string.
It can span multiple lines.
Useful for long text blocks."""
print(multi_line)
# raw multi-line string
raw_multi_line = r"""This is a raw multi-line string.
No escape sequences like \n or \t are processed."""
print(raw_multi_line)
# triple single quotes multi-line string
triple_single = '''This is another way to create
a multi-line string using triple single quotes.'''
print(triple_single)
# combining escape characters
print("First Line\nSecond Line\twith tab and a backslash \\")
print("Path to folder: C:\\Users\\Sivaram\\Documents\\Projects")
print(r"Raw string path: C:\Users\Sivaram\Documents\Projects")
# unicode and special characters
print("Smiley face: \u263A")
print("Copyright symbol: \u00A9")
print("Registered trademark: \u00AE")
print("Euro symbol: \u20AC")
# raw string with quotes
print(r'She said, "It\'s a raw string!"')
print(r"This is a raw string with \"double quotes\" and 'single quotes'.")







