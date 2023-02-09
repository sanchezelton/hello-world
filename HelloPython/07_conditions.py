# Lesson 7:
# Conditions (https://www.learnpython.org/en/Conditions)
# based on lessons available at www.learnpython.org

# Note, run with -W to suppress a warning generated on line 46, see comment

x = 2           # assignment, no value
print(x == 2)   # equality op, true 
print(x == 3)   # equality op, false
print(x < 3)    # less than op, true
print()

# 'and' and 'or' are used as boolean operators for complex boolean expressions, checked with if statements
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
print()

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")
print()

# 'in' operator checks a list against a variable
if name in ["John", "Rick"]:
    print("Your name is either John or Rick on my list")
print()

# else and elif are used to chain checks with blocks; note that is can be used to check for equality in an if statement
statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True: # else if
    pass
else:
    pass

# equality op and "is" are similar, but not exactly the same
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two")
print()

if x is 2:      # using 'is' with literals will show a warning, use with instances
    print("x is two!")
else:
    print("x is not two")
print()

# "is" will differ if the instances are not the same
x = [1, 2, 3]
y = [1, 2, 3]
print("x == y: %s" % (x == y))  # True
print("x is y: %s" % (x is y))  # False
print()

# you can use keyword "not" before a boolean expression to invert it
print(not False) # true
print((not False) == (False)) # false
print()

print("Exercise")

# Change the variables in teh first section, so that each if statement resolves to true

# change this code
# number = 10
# second_number = 10
# first_array = []
# second_array = [1,2,3]

number = 20
second_number = 0       # zero is considered false for ints in a boolean expression, non-zeroes are considered true
first_array = [1,17,52]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")