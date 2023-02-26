# game.py - mock for a game module
# import the draw module's functions into the current namespace

# METHOD 0 (no longer used for Python3, but important to know if working under Python 2.x)
# this is an _implicit_ _relative_ _import_ and is NO LONGER ALLOWED in python3 for modules (top level is OK)
# import draw

# METHOD 1
# ...so for python3 modules, we must use the from-implicit form of import to refer to other modules that this file belongs to
# NOTE: This will NOT work for a top level import!
from . import draw

# METHOD 2
# 1st alternative means to import: import a specific function within a module into the current namespace requires .moduleName syntax for explicit relative import
# (comment out line with annotated comment @about Functional and uncomment line with annotated comment @about ModuleReference )
# NOTE: This will NOT work for a top level import!
# from .draw import draw_game
# a white space between the leading dot and module name is OK and is functionally equivolent, e.g.
# from . draw import draw_game

# METHOD 3
# 2nd alternative, import all functions, classes, or variables within a module into the current namespace
# from . draw import *

# METHOD 4
# 3rd alternative, import a specific function within a module into the current namespace, under a different name/alias in the current namespace.
# For instance, let's say a game has a GUI drawing and text drawing modules implementing similarly named functions in their respective modules
# and we're dependent on a boolean flag visual_mode to switch between them:
# 
# if visual_mode:
#    import draw_visual as draw
# else:
#    import draw_textual as draw

def play_game():
     # do something
    return

def main():
    result = play_game()
    draw.draw_game(result)      # @about ModuleReference 
    # had the draw module's draw_game function been imported into the current namespace (see METHOD 2), invocation of draw_game would not include the module name
    # draw_game(result)         # @about Functional

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
