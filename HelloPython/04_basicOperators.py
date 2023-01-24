# Lesson 4:
# Basic Operators (https://www.learnpython.org/en/Basic_Operators)
# based on lessons available at www.learnpython.org

# arithmetic operators
number = 1 + 2 * 3 / 4.0
print(number)

# modulo operator
remainder = 11 % 3
print(remainder)

# power operator (**)
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# addition operator for string concatenation
helloworld = "hello" + " " + "world"
print(helloworld)

# multiplication of strings for repeating sequences
lotsofhellos = "hello" * 10
print(lotsofhellos)

# joining lists using addition operator
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# repeating lists can also be done as per string repeats
print([1, 2, 3] * 3)

print()
print("Exercise")

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y,
# respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by 
# concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
# x_list = [x]
# y_list = [y]
# big_list = []
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

