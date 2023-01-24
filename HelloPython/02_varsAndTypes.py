# Lesson 2:
# Variables and types (https://www.learnpython.org/en/Variables_and_Types)
# based on lessons available at www.learnpython.org

# no static typing, no need to declare variables before using them, nor declare their types
# every variable in python is an object

# integers
myint = 7
print(myint)

# floating point
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# strings with single quotes
mystring = "Don't worry about apostrophes"
print(mystring)

# sums and concatenation
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# single line, multiple assignment, multiple output
a, b = 3, 4
print(a, b)

# mixing operators between numbers and strings is NOT supported
one = 1
two = 2
hello = "hello"
# The print line below, when uncommented, errors out with
# Traceback (most recent call last):
#  File "/Users/sanchezelton/dev/hello-world/HelloPython/varsAndTypes.py", line xx, in <module>
#    print(one + two + hello)
#          ~~~~~~~~~~^~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(one + two + hello)

print()
print("Exercise:")

# Exercise:
# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring 
# and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, 
# and the integer should be named myint and should contain the number 20.

# solution

# change this code
# mystring = None
# myfloat = None
# myint = None
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
