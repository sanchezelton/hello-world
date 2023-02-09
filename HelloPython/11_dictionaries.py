# Lesson 11:
# Dictionaries (https://www.learnpython.org/en/Dictionaries)
# based on lessons available at www.learnpython.org

# Dictionaries are comparable to what are called objects in languages like JavaScript
# and is a specific kind of map ADT, using keys and values

# basic dictionary and adding entries
phonebook = {}  # instantiates an empty dictionary
phonebook["John"] = 14085551234     # adds one entry
phonebook["Jack"] = 14155551337     # adds a second entry
phonebook["Jill"] = 16505551984     # adds a third entry
print(phonebook)        # note that while the output appears to be JSON format, it only has single quotes for the keys, not double quotes

# combined declaration and instantitation plus iteration
emailContacts = { "John": "john@example.com", "Jack": "jack@example.net", "Jill": "jill@example.org"}    # declaration and instantiation
for name, email in emailContacts.items():
    print("E-mail address of %s is %s" % (name, email))
print()

# remove an entry using the del keyword
del phonebook["John"]
print("Removed John from phonebook")
print(phonebook)
print()

# the pop function can accomplish the same
emailContacts.pop("John")
print("Removed John from emailContacts")
print(emailContacts)
print()

print("Exercise")

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is in the phonebook")
if "Jill" not in phonebook:
    print("Jill is not in the phonebook")
