# Lesson 12:
# Modules and Packages (https://www.learnpython.org/en/Modules_and_Packages)
# based on lessons available at www.learnpython.org

# Modules group code into specific functionalities.

# Writing modules
# Modules in Python are just Python files with a .py extension. The module's name is the same as the file name
# (see mygame/draw.py and mygame/game.py files)
# When modules are grouped into folders, the subdirectory is a PACKAGE.

# by default, the .py file's directory is where imported modules are looked up if they do not match a core Python module

# To specify additional directories to search for modules when importing, the environment variable PYTHONPATH can be set.
# Note: This is not generally done in $HOME/.zshrc, /etc/profile or other shell RC or profile files, but when the
# python script is executed.
# Note: PYTHONPATH could be compared to CLASSPATH in Java
#
# Examples:
# e.g. PYTHONPATH=/foo python game.py
# 
# You can also use sys.path.append in Python source to set the lookup programatically. 
# Note that must be run before any import commands:
# 
# example:
import sys
sys.path.append("/foo")
import foo.bar
foo.bar.printFoobar()

# For the mygame directory mentioned above, mygame is the package containing the game and draw modules
# @see game.py and draw.py for examples of imports in this directory's mygame subdirectory
import mygame.game

# Core modules analysis

# there are the built in libraries (see https://docs.python.org/3/library/)
# let's try using urllib from python core libraries and explore its functions

# now we can use a function in it if we were using python 2.x
# import urllib
# urllib.urlopen("http://www.python.org")   # urllib.urlopen is DEPRECATED and DISCONTINUED in python 3.x

# under python3
import urllib.request

# using with is similar to the use statement in C#, this will close the connection automatically after it is done using it
# @see https://www.geeksforgeeks.org/with-statement-in-python/
# Note: If using MacOS X, you will need to install the required certifications for using urllib:qq
# $ sudo /Applications/Python\ 3.10/Install\ Certificates.command
print("Using with keyword syntax upon urllib.request.urlopen")
with urllib.request.urlopen("http://www.python.org", None) as url:
    # when the body callback executes, the data is then available as a http.client.HTTPResponse object
    s = url.read()
    print(s) # prints the HTML fetched from the page
print()

## without with, we'd be forced to close it manually
print("Without using with keyword syntax upon urllib.request.urlopen")
url = urllib.request.urlopen("http://www.python.org", None)
s = url.read()
print(s)
url.close()
print()

# we can see which functions are implemented in the module
print("urllib.request functions:")
print(dir(urllib.request))
print()

# we can also lookup information about a function (scroll up/down/left/right w/ arrow keys, Q to quit), note this doesn't return a string but a textual modal (press q in the terminal to quit)
help(urllib.request.urlopen)

print()
print("Execise")

# In this exercise, print an alphabetically sorted list of all the functions in the re module containing the word find.

import re
find_members = []
for fn in dir(re):
    if fn.count("find") > 0:
        find_members.append(fn)
find_members.sort()
print(find_members)
