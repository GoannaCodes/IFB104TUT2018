# "Curves" module
#
# In this file you will define a function which draws a
# single curved shape on the screen, starting from the
# "home" coordinate, at a given angle and with a certain
# radius.  This function will be imported into,
# and called by, the "main" Curves program.

from turtle import *

# Define a Turtle graphics function which has two
# parameters, a heading (in degrees) and a radius (in
# pixels).  When called the function should go to the
# home position, set the turtle's heading to the given
# angle, walk part of a circle, and return to the
# home position.  Initially, try setting the "extent"
# of the circle walked to 70 degrees.  (You can vary
# this later to get different effects.)

#### Define your function for drawing a curved
#### shape here
def curve(angle, radius):
    penup() #don't start drawing yet
    home() #go home (0, 0)
    setheading(angle) #turtle facing a given angle
    pendown() #start drawing
    circle(radius, extent = 225) #draw a circle of given radius up to 70 degrees
    penup() #stop drawing
    home() #go back home (0, 0)
