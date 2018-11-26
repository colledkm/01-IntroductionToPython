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

for k in range(45) :
    tully.draw_circle(size)
    tully.left(92)
    tully.forward(k)

    mo.forward(size * 0.5)
    mo.backward(size)
    mo.forward(size * 0.5)
    mo.left(92)

mo.pen = rg.Pen('purple',5)
mo.speed = 100
mo.pen_up()
mo.forward(200)
mo.right(90)
mo.backward(125)
mo.right(90)
mo.forward(75)
mo.left(90)
mo.left(90)
mo.pen_down()

for k in range (100) :
    mo.forward(size * 0.5)
    mo.backward(size)
    mo.left(92)

rebecca = rg.SimpleTurtle('turtle')
rebecca.pen = rg.Pen('midnight blue',2)
rebecca.pen_up()
rebecca.right(120*0.5)
rebecca.pen_down()
rebecca.speed = 500

for k in range(50):
    for k in range(3):
        rebecca.forward(150)
        rebecca.left(120)
    rebecca.right(92)


window.close_on_mouse_click()
