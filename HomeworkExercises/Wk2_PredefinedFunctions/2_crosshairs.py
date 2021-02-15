# Crosshairs - Draw a "gunsight" crosshair image
#
# As practice in drawing an image using Turtle graphics, draw the
# familiar image of a gunsight's crosshairs, consisting of a
# cross formed from two lines, plus a circle.  To make it interesting,
# we will aim the crosshairs at an evil alien monster intent on
# destroying the Earth!
#
# The monster will appear in the background image when you run this
# file.  We haven't told you the Turtle coordinates at which the
# monster appears, so you will need to use some trial-and-error to
# find its centre.
#
# Comment: The image of the alien has deliberately been placed
# off-centre.  Therefore you will need to draw the crosshairs
# at this location instead of the default origin in the middle of
# the screen.  Although you could do so using absolute coordinates,
# you are encouraged to move the turtle to the monster's centre
# and then draw the crosshairs relative to this point.  This will
# make your program easier to maintain if, for instance, we wanted
# to use it with another picture of a monster in a different
# location.
#
# NB: Ensure that the GIF file with the monster's image is in
# the same folder (directory) as this Python program.


# A SOLUTION
#
# Problem-solving strategy:
# 0. Some predefined preliminaries

from turtle import * # import turtle graphics
setup(600, 600) # set the window size to match the image
bgpic("monster.gif") # add the image of the monster
title("Beware of the monster!") # add a title to the window
width(3) # ensure the crosshairs will be easily visible

# 1. Move the turtle to the monster's centre (without drawing)
penup()
goto(-145, 0)
setheading(270)
forward(130)

# 2. Draw the vertical line centred on the current position (and
#    return to the starting point)
#move turtle to the left from the center
setheading(180) #cursor facing left
forward(130) 
#draw vertical line from left to right
pendown()
setheading(360)
forward(260)
penup()
#move back to center
setheading(180)
forward(130)

# 3. Draw a horizontal line centred on the current position (and
#    return to the starting point)
#move turtle ontop of monster
setheading(90)
forward(130)
#draw horizontal line from top to bottom
pendown()
setheading(270)
forward(260)
penup()
#move back to center
setheading(90)
forward(130)

# 4. Draw  the crosshair's circle centred on the current position
#move halfway up top half of horizontal line
setheading(270)
forward(65)
setheading(0)
pendown()
circle(65)
# 5. Exit the program by hiding the turtle and releasing the
#    drawing window
hideturtle()
done()
