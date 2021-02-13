# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.

#import the turtle graphics function
from turtle import * #import everything from the turtle module
from random import randint #picks a random integer

#set up drawing canvas
setup()
penup() #don't start drawing yet

#define radius of circles
radius = [25, 40, 75] #will pick a random integer for the radius of the circle

#start drawing first circle
pendown()
pencolor('red')
circle(radius[0])
penup() #stop drawing before moving to new location

#moving turtle cursor
forward(radius[0] + 150) #move forward by 150 pixels + radius of circle
left(90) #turn left 90 degrees

#start drawing second circle
pendown()
pencolor('blue')
circle(radius[1])
penup()

#moving turtle cursor
home()
setheading(180)
forward(radius[1] + 150)
left(90)

#start drawing third circle
pendown()
pencolor('green')
circle(radius[2])
penup()

#receiving type error for int in circle(radius) which can't be called
hideturtle()
done()
