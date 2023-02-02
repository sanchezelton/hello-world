# Lesson 5:
# String Formatting (https://www.learnpython.org/en/String_Formatting)
# based on lessons available at www.learnpython.org

# String formatting simple
name = "John"
print("Hello, %s!" % name)

# Two or more arguments need a tuple; integers are formatted with %d instead of %s
name = "James"
age = 23
print("%s is %d years old." % (name, age))

# non strings are formatted using %s. The string which returns from the "repr" method of that object is
# formatted as the string
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# %f formats floating point numbers - %.12f, for example formats a floating point number to 12 digits after the decimal point
pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410
print("Pi is about %.2f" % pi)

# %x or %X - formats integers in hex (lowercase or uppercase respectively)
ten = 31211
print("31211 in capped hex is %X" % ten)
print("31211 in non-capped hex is %x" % ten)

print()
print("Exercise")

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
# format_string = "Hello"
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)
