# Lesson 3:
# Lists (https://www.learnpython.org/en/Lists)
# based on lessons available at www.learnpython.org

# can contain any type of variable and contain as many as deired

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

# iterate through items in a list
for x in mylist:
    print(x)

# accessing an index which does not exist generates an exception
mylist = [1,2,3]
# The print line below, when uncommented, errors out with
# Traceback (most recent call last):
#  File "/Users/sanchezelton/dev/hello-world/HelloPython/03_lists.py", line xx, in <module>
#    print(mylist[10])
#          ~~~~~~^^^^
# IndexError: list index out of range
# print(mylist[10])

print()
print("Exercise")

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the
# numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
# 
# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator [].
# Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
# second_name = None
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

