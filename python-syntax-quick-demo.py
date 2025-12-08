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

# raw string completly ignores escape sequences.

# slicing strings
sample_str = "Hello, World!"
print("Original string:", sample_str)
# slicing from index 0 to 4
print("Sliced string (0 to 4):", sample_str[0:5])
# slicing from index 7 to end
print("Sliced string (7 to end):", sample_str[7:])
# slicing with step
print("Sliced string with step 2:", sample_str[::2])
# reverse slicing
print("Reversed string using slicing:", sample_str[::-1])
# slicing with negative indices
print("Sliced string using negative indices (-6 to -1):", sample_str[-6:-1])
# slicing with start and end omitted
print("Sliced string with start omitted (to index 4):", sample_str[:5])
print("Sliced string with end omitted (from index 7):", sample_str[7:])
# slicing with negative step
print("Sliced string with negative step (-1):", sample_str[:: -1])
# substring extraction
substring = sample_str[7:12]
print("Extracted substring (7 to 11):", substring)
# slicing with variables
start_index = 0
end_index = 5
sliced_with_vars = sample_str[start_index:end_index]
print("Sliced string using variables (0 to 4):", sliced_with_vars)
# slicing to get every 3rd character
print("Every 3rd character from string:", sample_str[::3])
# slicing with complex indices
print("Sliced string (1 to -1) with step 2:", sample_str[1:-1:2])
# slicing empty string
empty_str = ""
print("Slicing empty string:", empty_str[0:5])  # should return empty
# slicing single character string
single_char_str = "A"
print("Slicing single character string:", single_char_str[0:1])  # should return 'A'
# slicing with out of range indices
print("Slicing with out of range indices (0 to 50):", sample_str[0:50])  # should return full string
# slicing with start greater than end
print("Slicing with start greater than end (5 to 0):", sample_str[5:0])  # should return empty string
# slicing with step zero (should raise error)
# print("Slicing with step zero:", sample_str[::0])  # Uncommenting this line will raise a ValueError
# slicing unicode string
unicode_str = "こんにちは世界"  # "Hello World" in Japanese
print("Slicing unicode string (0 to 4):", unicode_str[0:5]) # should return 'こんにちは'    
# slicing string with special characters
special_str = "Hello, @World#2024!"
print("Slicing string with special characters (7 to 12):", special_str[7:12]) # should return '@Worl'
# slicing long string
long_str = "This is a long string used for demonstrating slicing in Python."
print("Slicing long string (10 to 30):", long_str[10:30]) # should return 'long string used for'
# slicing string with spaces
space_str = "   Leading and trailing spaces   "
print("Slicing string with spaces (3 to -3):", space_str[3:-3]) # should return 'Leading and trailing spaces'
# string with in and not in operators
test_str = "The quick brown fox jumps over the lazy dog"
print("'quick' in test_str?", 'quick' in test_str)
print("'cat' not in test_str?", 'cat' not in test_str)
print("'lazy' in test_str?", 'lazy' in test_str)
print("'elephant' not in test_str?", 'elephant' not in test_str)
# checking substrings
print("'The' in test_str?", 'The' in test_str)
print("'fox' not in test_str?", 'fox' not in test_str)
print("'jumps' in test_str?", 'jumps' in test_str)
print("'wolf' not in test_str?", 'wolf' not in test_str)
# checking empty string
empty_check = ""
print("Is empty string in test_str?", empty_check in test_str)
print("Is empty string not in test_str?", empty_check not in test_str)
# checking case sensitivity
print("'the' in test_str?", 'the' in test_str)  # should be False
print("'The' in test_str?", 'The' in test_str)  # should be True
# checking special characters
special_check = "@"
print("Is '@' in test_str?", special_check in test_str)  # should be False
print("Is '#' not in test_str?", '#' not in test_str)  # should be True
# checking numeric substrings
numeric_str = "123"
print("Is '123' in numeric_str?", '123' in numeric_str)  # should be True
print("Is '456' not in numeric_str?", '456' not in numeric_str)  # should be True
# checking longer substrings
long_substr = "quick brown fox"
print("Is 'quick brown fox' in test_str?", long_substr in test_str)  # should be True
print("Is 'lazy cat' not in test_str?", 'lazy cat' not in test_str)  # should be True
# checking substrings with spaces
space_substr = "over the"
print("Is 'over the' in test_str?", space_substr in test_str)  # should be True
print("Is 'under the' not in test_str?", 'under the' not in test_str)  # should be True 

# string methods
sample_string = "  Hello, World! Welcome to Python programming.  "
print("Original string:", sample_string)
# strip whitespace
print("String after strip():", sample_string.strip())
# lower case
print("String after lower():", sample_string.lower())
# upper case
print("String after upper():", sample_string.upper())
# string is upper
print("Is the string upper case?", sample_string.isupper())
# string is lower
print("Is the string lower case?", sample_string.islower())
# title case    
print("String after title():", sample_string.title())
# replace substring
print("String after replace('World', 'Universe'):", sample_string.replace("World", "Universe"))
# split string
print("String after split():", sample_string.split())
# find substring
print("Index of 'Python' in string:", sample_string.find("Python"))
# count substring occurrences
print("Count of 'o' in string:", sample_string.count("o"))
# startswith    
print("Does string start with '  Hello'?", sample_string.startswith("  Hello"))
# endswith
print("Does string end with 'programming.  '?", sample_string.endswith("programming.  "))
# isalpha
print("Is 'Hello' alphabetic?", "Hello".isalpha())
# isdigit
print("Is '12345' numeric?", "12345".isdigit())
# isspace
print("Is '   ' whitespace?", "   ".isspace())
# capitalize
print("String after capitalize():", sample_string.capitalize())
# title case
print("String after title():", sample_string.title())
# center string
print("String after center(50, '*'):", sample_string.center(50, '*'))
# join strings
words = ["Hello", "from", "Python"]
print("Joined string with space:", " ".join(words))
# zfill
print("String after zfill(30):", sample_string.strip().zfill(30))
# partition
print("String after partition('World'):", sample_string.partition("World"))
# rpartition
print("String after rpartition('o'):", sample_string.rpartition("o"))
# swapcase
print("String after swapcase():", sample_string.swapcase())
# expandtabs
tabbed_string = "Hello\tWorld\tPython"
print("String after expandtabs(4):", tabbed_string.expandtabs(4))
# formatting with f-strings
name = "Sivaram"
age = 30
print(f"My name is {name} and I am {age} years old.")
# formatting with format()
print("My name is {} and I am {} years old.".format(name, age))
# formatting with % operator
print("My name is %s and I am %d years old." % (name, age))

# raise exception
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
# test the function 
try:
    result = divide(10, 0)
    print("Result of division:", result)
except ValueError as e:
    print("Error occurred:", e)

# custom exception
class NegativeValueError(Exception):
    pass    
    def square_root(x):
        if x < 0:
            raise NegativeValueError("Cannot compute square root of negative value.")
        return x ** 0.5
    try:
        result = square_root(-25)
        print("Square root:", result)
    except NegativeValueError as e:
        print("Error occurred:", e)

# raise custom exception
raise NegativeValueError("This is a custom negative value error.")
# Note: The above line will raise the exception when executed.
# raise general exception
raise Exception("This is a general exception.")
# Note: The above line will raise the exception when executed.

# assert statement
def calculate_average(numbers):
    assert len(numbers) > 0, "The list of numbers cannot be empty."
    return sum(numbers) / len(numbers)  
# test the function
try:
    avg = calculate_average([])
    print("Average:", avg)
except AssertionError as e:
    print("Assertion Error:", e)
# successful assertion
try:
    avg = calculate_average([10, 20, 30])
    print("Average:", avg)
except AssertionError as e:
    print("Assertion Error:", e)    

# raise assertion error
assert 2 + 2 == 5, "Math is broken!"
# Note: The above line will raise an AssertionError when executed.
# successful assertion
assert 2 + 2 == 4, "Math is still working!"
print("Assertion passed: Math is working correctly.")

# import logging module
import logging
# configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# log messages of different severity levels
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
# log an exception
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.exception("An exception occurred: %s", e)
# custom logger
logger = logging.getLogger("customLogger")
logger.setLevel(logging.INFO)
# create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
# add handler to logger
logger.addHandler(console_handler)
# log messages using custom logger
logger.info("This is an info message from custom logger.")
logger.error("This is an error message from custom logger.")
# log messages with variables
user = "Sivaram"
action = "login"
logger.info("User %s performed %s action.", user, action)
# log a warning with variables
disk_space = 5  # in percentage
logger.warning("Low disk space: %d%% remaining.", disk_space)
# log a critical error
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    logger.critical("Critical error: %s", e)
# Note: The above code will log messages to the console when executed.

# lamda functions
# simple lambda function to add two numbers
add = lambda x, y: x + y
result = add(5, 10)
print("Sum of 5 and 10 using lambda function:", result)
# lambda function to square a number
square = lambda x: x ** 2
result = square(6)
print("Square of 6 using lambda function:", result)
# lambda function with multiple parameters
multiply = lambda x, y, z: x * y * z
result = multiply(2, 3, 4)
print("Multiplication of 2, 3 and 4 using lambda function:", result)
# lambda function with no parameters
greet = lambda: "Hello, World!"
message = greet()
print("Greeting message using lambda function:", message)
# using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using lambda with map():", squared_numbers)
# using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda with filter():", even_numbers)
# using lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using lambda with reduce():", product)


# lamda function without name
result = (lambda x, y: x - y)(10, 4)
print("Result of subtraction using unnamed lambda function:", result)
# lambda function returning another function
def make_incrementer(n):
    return lambda x: x + n
increment_by_5 = make_incrementer(5)
result = increment_by_5(10)
print("Result of incrementing 10 by 5 using lambda function:", result)

# make adder function using lambda
def make_adder(n):
    return lambda x: x + n
add_10 = make_adder(10)
result = add_10(5)
print("Result of adding 10 to 5 using lambda function:", result)

# ternary operator
a = 10
b = 20
max_value = a if a > b else b
print("Maximum value between a and b using ternary operator:", max_value)
# another example
num = 15
parity = "Even" if num % 2 == 0 else "Odd"
print("The number is:", parity)

# passing multiple parameters to function using *argumnets
def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string + " "
    return result.strip()
concatenated = concatenate_strings("Hello", "from", "Python", "functions")
print("Concatenated string using *arguments:", concatenated)
# passing multiple keyword arguments using **kwargs
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_person_info(name="Sivaram", age=30, city="New York")
# passing list to function using *arguments
def sum_numbers(*args):
    return sum(args)
total = sum_numbers(1, 2, 3, 4, 5)
print("Sum of numbers using *arguments:", total)
# passing dictionary to function using **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
info = {"name": "Sivaram", "age": 30, "city": "New York"}
display_info(**info)
# combining *args and **kwargs in function
def combined_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
combined_function(1, 2, 3, name="Sivaram", age=30)
# unpacking list and dictionary while calling function
def sample_function(a, b, c, name, age):
    print(f"a: {a}, b: {b}, c: {c}, name: {name}, age: {age}")
num_list = [10, 20, 30]
person_info = {"name": "Sivaram", "age": 30}
sample_function(*num_list, **person_info)
# using * to unpack list in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in [*fruits]:
    print("Fruit from unpacked list in for loop:", fruit)
# using ** to unpack dictionary in function call
def greet_person(name, age):
    print(f"Hello, {name}. You are {age} years old.")
person_dict = {"name": "Sivaram", "age": 30}
greet_person(**person_dict)
# using * to unpack string into list
def print_characters(*args):
    for char in args:
        print("Character from unpacked string:", char)
sample_string = "Hello"
print_characters(*sample_string)
# using ** to unpack nested dictionary
def display_address(street, city, country):
    print(f"Street: {street}, City: {city}, Country: {country}")
address_dict = {"street": "123 Main St", "city": "New York", "country": "USA"}
display_address(**address_dict)
# combining *args and regular parameters
def mixed_parameters(x, y, *args):
    print(f"x: {x}, y: {y}, args: {args}")
mixed_parameters(1, 2, 3, 4, 5)
# combining **kwargs and regular parameters
def mixed_kwargs(name, age, **kwargs):
    print(f"name: {name}, age: {age}, kwargs: {kwargs}")
mixed_kwargs("Sivaram", 30, city="New York", profession="Engineer")
# using * to unpack set in function call
def print_set_elements(*args):
    for element in args:
        print("Element from unpacked set:", element)
sample_set = {1, 2, 3}
print_set_elements(*sample_set)

# switch case using match-case
def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

# test the function
day_name = day_of_week(3)
print("Day of the week for day 3 is:", day_name)






