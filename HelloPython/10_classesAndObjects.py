# Lesson 10:
# Classes and Objects (https://www.learnpython.org/en/Classes_and_Objects)
# based on lessons available at www.learnpython.org

# objects are an encapsulation of variables and functions into a single entity
# objects get their variable and functions from classes.

# basic class definition
class MyClass:
    variable = "blah"

    def function(self): # member functions always have a self parameter first
        print("This is a message inside the class")

# instatiating an object from the class
myobjectx = MyClass()

# access an object's variable and functions uses dot notation (as opposed to dictionaries, TBD, which use brackets only)
print(myobjectx.variable)       # echoes blah to stdout
myobjectx.variable              # value unpacked, but not echoed to stdout
myobjectx.function()            # invokes MyClass.function member function
print()

# each instance will have its own member variables instantiated and can be set
myobjecty = MyClass()
myobjecty.variable = "yakity yak"
print("myobjecty.variable: %s" % myobjecty.variable)
print("mybojectx.variable: %s" % myobjectx.variable)
print()

# a reserved name __init__ function serves as a the constructor function for the class
class NumberHolder:
    def __init__(self, number):
        self.number = number

holderInstance = NumberHolder(1999)
print("holderInstance.number: %s" % holderInstance.number)
print()

print("Exercise")

# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth 
# $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.color = "red"
car1.kind = "convertible"
car1.name = "Ferrari"
car1.value = 60000

car2 = Vehicle()
car2.color = "blue"
car2.kind = "van"
car2.name = "Dodge"
car2.value = 10000

print(car1.description())
print(car2.description())
