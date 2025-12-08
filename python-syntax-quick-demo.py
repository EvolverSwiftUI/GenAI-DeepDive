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












