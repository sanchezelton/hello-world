# draw.py - mock for a real drawing module

def draw_game(content):
    # clear the screen
    clear_screen(main_screen)
    # draw the next frame
    return

def clear_screen(screen):
    screen.clear()
    return

class Screen:
    def clear(self):
        # clear the screen
        return

# the code in the module is executed only once, the first time it is imported (so in this case, main_screen is a singleton)
# Note: In most cases though, this is a bad practice and should be avoided as it can create unintended side-effects.
main_screen = Screen()
print("mygame/draw.py: Screen initialized")     # this should only appear once
