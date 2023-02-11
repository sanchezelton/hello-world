# Lesson 12:
# Modules and Packages (https://www.learnpython.org/en/Modules_and_Packages)
# based on lessons available at www.learnpython.org

# Modules group code into specific functionalities.

# Writing modules
# Modules in Python are just Python files with a .py extension. The module's name is the same as the file name
# (see mygame/draw.py and mygame/game.py files)

# the environment variable PYTHONPATH can be set to specify additional direcoties to look for modules
# programatically, you can also use sys.path.append. Note it must be run before any import commands:
# 
# example:
# sys.path.append("/foo")

# there are the built in libraries (see https://docs.python.org/3/library/)
# let's try using urllib and explore its functions

# now we can use a function in it if we were using python 2.x
# import urllib
# urllib.urlopen("http://www.python.org")   # urllib.urlopen is DEPRECATED and DISCONTINUED in python 3.x

# under python3
import urllib.request
import mygame.game

# using with is similar to the use statement in C#, this will close the connection automatically after it is done using it (similar to await??)
with urllib.request.urlopen("http://www.python.org") as url:
    # when the body callback executes, the data is then available as a http.client.HTTPResponse object
    s = url.read()
    print(s) # prints the HTML fetched from the page
print() # because of with keyword, this is fetched after the callback completes

# we can see which functions are implemented in the module
print(dir(urllib.request))
print()

# we can also lookup information about a function (scroll up/down/left/right w/ arrow keys, Q to quit), note this doesn't return a string but a textual modal
help(urllib.request.urlopen)

