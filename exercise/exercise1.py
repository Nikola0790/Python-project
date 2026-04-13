# How to find the integer part of a floating point number and how to convert a text string to a number?
a = 100 / 33
print(int(a))  # Display the integer part

b = "2017"
year = int(b)
print("The year is", year)

# How to create a set of numbers from 0 to 10?
a = range(0, 11)

# How to draw a number from 10 to 20?
from random import randint

# How to split a string to a list?
my_str = "A long time ago, in a galaxy far, far away..."
my_list = my_str.split()

# How to combine a list of words into a single text string?
my_list = ['A', 'long', 'time', 'ago,', 'in', 'a', 'galaxy', 'far,', 'far', 'away...']
my_str = " ".join(my_list)

# How to convert a letter from lowercase to uppercase?
txt = "a new hope"
txt2 = txt.upper()
txt3 = "empire strikes back".upper()
print(txt2, txt3)

# How to create a list of numbers in a given range?
a = range(0, 10)
b = list(a)

# How to draw three different numbers from a range?
from random import shuffle

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
shuffle(a)
print(a[:3])

rnd = randint(10, 20)
print(rnd)

# Exercise 1
import random

random_number = random.randint(0, 10)
for i in range(random_number):
    print("*", end="")
print()

# Exercise 2
# Declare the variables rows and columns that will store random numbers between 5 and 15.
# Display the numbers on the screen.
# Display a rectangle of the drawn sizes, made up of stars (*).

rows = random.randint(5, 10)
columns = random.randint(5, 10)

print("Rows: ",rows)
print("Columns: ",columns)

# draw the rectangle
for i in range(rows):
    line = ""
    for j in range(columns):
        line = line + "*"
    print(line)

# Exercise 3
# Declare the variable size that will store a random number between 3 and 9.
# Display the drawn number on the screen.
# Display a Christmas tree of the drawn size, made of stars (*).
# Do not use string multiplication when solving this exercise! Instead, use 2 loops.

x = random.randint(3, 9)
print("Drawn number: ", x)

for i in range(x):
    line=""
    for j in range(i):
        line = line + "*"
    print(line)

# Write a function multiply(subject, times) that returns the value of the variable subject
# multiplied by the value of the argument times. 
# Note what happens if you type a number as the value of argument subject, and what if you type a string.
print('FUNCTIONS')
def multiply(subject, times):
    return subject * times
print(multiply(5, 5))
print(multiply(5, "test"))

def power(x, y=2):
    return x * y
print(power(5))

def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
print(to_celsius(100))

for a, b in zip([1,2,5], [3,4,6]):
    print(a, b)

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

# Exercise 5
# Write a function chessboard that takes an optional parameter n. 
# The standard value of the parameter should be 8. 
# The function will return a multiline string representing a chessboard composed of # characters and spaces. 
# The chessboard should have dimensions n x n.

# Example: For n=8, the chessboard should consist of 8 lines, each with 8 characters: alternating # and space.

def chessboard (n):
    board = ''
    for i in range(n):
        line = ''
        for j in range(n):
            if (i + j) % 2 == 0:
                line += "#"
            else: 
                line += ' '
        board += line + "\n"
    return board
print(chessboard(8))

#LIST AND TUPLES
def create_list (x, y):
    count = 1
    list = []
    while count < 5:
        list.append(x)
        list.append(y)
        count += 1
    
    return list

print(create_list(1, 2))

person = {
    "name": "Ana",
    "age": 17,
    "city": "Belgrade"
}

def list_keys(d):
    list = []
    for key in d:
        list.append(key)
    return list


print(list_keys(person))

def find_short_words(list):
    newList = []
    for item in list:
        if len(item) < 5:
            newList.append(item)
    return newList

print(find_short_words(['itsy', 'bitsy', 'spider', 'climbed', 'up', 'the', 'waterspout']))

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

def message(dictionary):
    if not all (key in input_dict for key in ['name', 'role', 'movie']):
        return None
    else:
        return "In {}, {} is a {}.".format(dictionary['movie'], dictionary['name'], dictionary['role'])

print(message(input_dict))

#Tommorow Date

import datetime

def tommorow():
    return datetime.date.today() + datetime.timedelta(days=1)

print(tommorow())

from coderslab import coderslab_welcome
coderslab_welcome()

from math_tools.functions import quadratic_function
print(quadratic_function(5, 5, 2, 7))