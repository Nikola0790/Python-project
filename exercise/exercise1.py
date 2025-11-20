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
