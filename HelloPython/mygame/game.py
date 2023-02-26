# game.py - mock for a game module
# import the draw module's functions into the current namespace

# this is an _implicit_ _relative_ _import_ and is NO LONGER ALLOWED in python3, but was under python2.x
# import draw

# so for python3, we must use the from-implicit form of import to refer to this module
from . import draw

# alternative means to import a specific function within a module into the current namespace
# from draw import draw_game

# 2nd alternative, import all functions, classes, or variables within a module into the current namespace
# from draw import *

# 3rd alternative, import a specific function within a module into the current namespace, under a different name.
# For instance, let's say a game has a GUI drawer and text drawer modules implementing similarly named functions in their respective modules
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
    draw.draw_game(result)
    # had the draw module's draw_game function been imported into the current namespace (see line 6 or line 9), invocation of draw_game would not include the module name
    # draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
