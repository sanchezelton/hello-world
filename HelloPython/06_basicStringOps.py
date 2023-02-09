# Lesson 6:
# Basic string operations (https://www.learnpython.org/en/Basic_String_Operations)
# based on lessons available at www.learnpython.org

# defining strings, w/ and w/o quotes
astring = "Hello world!"
astring2 = 'Hello world!'

print("single quotes are ' '")

# this prints out 12 because "Hello world!" is 12 characters long, including punctuation and spaces
print(len(astring))
print()

# this prints out 4 because the first occurance occurs as the 5th character; strings indexes are zero-based, so invoking .index("H") returns zero.
print(astring.index("o"))
print(astring.index("H"))
print()

# this counts the number of occurances of a character in a string, in this case 3 for the lowercase letter for L
print(astring.count("l"))
print()

# this prints a slice of a string, starting at index 3 and ending at index 6 (e.g. 7, non-inclusive), in the case the substring "lo w"
print("invoking astring[3:7]...")
print("selection:")
print("0....5....A....E")
print("   ____")
print(astring)
print(astring[3:7])
print()

# this also prints a slice, but from the beginning and up to the index (again, non-inclusive), in the case the substring "Hello w"
print("invoking astring[:7]...")
print("selection:")
print("0....5....A....E")
print("_______")
print(astring)
print(astring[:7])
print()

# this also prints a slice, but from the index to the end of the string, in the case the substring "orld!"
print("invoking astring[7:]...")
print("selection:")
print("0....5....A....E")
print("       _____")
print(astring)
print(astring[7:])
print()

# negative numbers work as well to signify the number of characers from the end, this printing only "d!"
print("invoking astring[-2:]...")
print("selection:")
print("0....5....A....E")
print("          __")
print(astring)
print(astring[-2:])
print()

# this negative number prints the characters up to the 2nd index from the end, printing "Hello worl"
print("invoking astring[:-2]...")
print("selection:")
print("0....5....A....E")
print("__________  ")
print(astring)
print(astring[:-2])
print()

# and this form is [start:stop:step], to step on over every other character, starting with the second L in "Hello", ending with "d" in world, but only printing every other character "l ol"
print("invoking astring[3:11:2]...")
print("selection:")
print("0....5....A....E")
print("   _ _ _ _ ")
print(astring)
print(astring[3:11:2])
print()

# this form prints characters from 3 to 7, but skipping no characters. (e.g. indices 3, 5, 7 [non-inclusive]); note this is the same as astring[3:7]
print("invoking astring[3:7:1]...")
print("selection:")
print("0....5....A....E")
print("   ____")
print(astring)
print(astring[3:7:1])
print("invoking astring[3:7]...")
print(astring[3:7])
print()

# this step can also be used to count backwards, so to reverse a string...
print("invoking astring[::-1]...")
print("selection:")
print("0....5....A....E")
print("<----------^")
print(astring)
print(astring[::-1])
print()

# these can respectively convert all letters to upper or lower case
print(astring.upper())
print(astring.lower())
print()

# and these functions check patterns in the given string
print(astring.startswith("Hello"))  # true
print(astring.endswith("saldfkdsl")) # false
print()

# finally, this string function splits a string into a list by a delimiter
print(astring.split(" "))
print()

print("Exercise")

# Try to fix the code to print out the correct information by changing the string.

# s = "Hey there! what should this string be?"
s = "It oughta be 20 ales"
print("S is '%s'" % s)
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
# if s.startswith("Str"):
if s.startswith("It ought"):
    print("String starts with 'It ought'. Good!")
    # print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("les"):
    print("String ends with 'les'. Good!")
    # print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
