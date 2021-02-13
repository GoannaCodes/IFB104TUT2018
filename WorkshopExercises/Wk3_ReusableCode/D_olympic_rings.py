#-------------------------------------------------------------------------
#
#  Olympic Rings
#
#  In this folder you will find a file "olympic_rings.pdf" which shows
#  the flag used for the Olympics since 1920.  Notice that this flag
#  consists of five rings that differ only in their position and colour.
#  If we want to draw it using Turtle graphics it would therefore be
#  a good idea to define a function that draws one ring and reuse it
#  five times.
#
#  Complete the code below to produce a program that draws a reasonable
#  facsimile of the Olympic flag.  (NB: In the real flag the rings are
#  interlocked.  Don't try to reproduce this tricky feature, just draw
#  rings that overlap.)
#


#-------------------------------------------------------------------------
#  Step 1: Function definition
#
#  Define a function called "ring" that takes three parameters, an
#  x-coordinate, a y-coordinate and a colour.  When called this function
#  should draw an "olympic ring" of the given colour centred on the
#  given coordinates.  (Note that Turtle graphic's "circle" function
#  draws a circle starting from the cursor's current position, not
#  centred on the cursor's position.)  Since all the circles are the
#  same size you can define the radius and thickness of the circle
#  within the function.

#  Import the Turtle functions
from turtle import *

###  PUT YOUR FUNCTION DEFINITION HERE
def ring(x_coord, y_coord, color):
    pencolor(color)
    width(10)
    #set position of outer ring
    penup() #stop drawing
    goto(x_coord, y_coord) #go to position of parameters
    goto(60 + x_coord, y_coord)
    setheading(90)

    #start drawing outer ring
    pendown()
    circle(60)
    penup() #stop coloring 
    
#-------------------------------------------------------------------------
#  Step 2: Calling the function
#
#  Now write code to call the function five times, each time with
#  different coordinates and colours, to create the flag.  To get
#  you started we have provided some of the Turtle framework.

#  Create the drawing window
setup(1000, 650)
title('"... and it\'s gold, Gold, GOLD for Australia!"')

# Draw the five rings
ring(0, 0, 'blue') #draw first ring
ring(135, 0,'black') #draw second ring
ring(270, 0, 'red') #draw third ring
ring(65, -70, 'yellow') #draw forth ring
ring(200, -70, 'green') #draw fifth ring

#  Shut down the drawing window
hideturtle()
done()
