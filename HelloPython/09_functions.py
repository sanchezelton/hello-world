# Lesson 9:
# Functions (https://www.learnpython.org/en/Conditions)
# based on lessons available at www.learnpython.org

# in python a block is defined in the following format
# block_head:
#   1st block line
#   2nd block line
#   ...

# genearal block_head line format is:
# <block_keyword> ?[<block_name>(argument1, argument2, ...)]?:
#
# examples of such are:
#
# if bool_expression:
# 
# for current in line:
#
# for i = 0 in range(x):
#
# while n < m:


# def keyword is used to define functions
def my_function():
    print("Hello From My Function!")

# defining a function returns no value and has no effect until it is invoked
my_function()
print()

# functions can also take arguments
def my_function_with_args(username, greeting):
    s = "Greetings, %s! %s" % (username, greeting)
    print(s)
my_function_with_args("Professor Falkan", "Would you like to play a game?")
print()

# functions can also return a value
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(10, 7))
print()

print("Exercise")

# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# Run and see all the functions work together!

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(info):
    return "%s is a benefit of functions!" % info

def name_the_benefits_of_functions():
    benefitsList = list_benefits()
    for benefit in benefitsList:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

