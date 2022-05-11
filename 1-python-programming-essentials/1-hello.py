"""
1 - docstring and comment
use """ """ to docstring -document string - to explain the purpose of this file
use # # to comment out short sentence in one line - explain the following code

2 - tools
what is an IDE - integrated development environment - software application to write, save and run programs
controls - code pane - console
1. CodeSkulptor3 - py3.codeskulptor.org
2. Thonny - install Thonny
3. Atom - install python, then atom
"""

"""
print hello as your first python code
"""
print("hello, world!")

# have a try below

import simplegui
message = "Welcome!"
# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
