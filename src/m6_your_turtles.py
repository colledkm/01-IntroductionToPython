"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Katana Colledge.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

tully = rg.SimpleTurtle('turtle')
tully.pen = rg.Pen('green', 5)
tully.speed = 50

mo = rg.SimpleTurtle('turtle')
mo.pen = rg.Pen('orange',5)
mo.speed = 50

size = 500

for k in range(50) :
    tully.draw_circle(size)
    tully.left(92)
    tully.forward(k)

    mo.forward(size * 0.5)
    mo.backward(size)
    mo.forward(size * 0.5)
    mo.left(92)

tully.pen = rg.Pen('midnight blue',5)
mo.pen = rg.Pen('purple',5)

for k in range (50) :
    mo.forward(size * 0.5)
    mo.backward(size)
    mo.left(92)



window.close_on_mouse_click()
