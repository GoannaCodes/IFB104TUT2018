#---------------------------------------------------------
#
#  Concentric Circles
#
#  In an earlier workshop exercise you developed a program
#  which drew three concentric circles.  Here we will
#  illustrate the power of repetitive code by developing
#  functions that draw as many circles as we want.
#
#  In this exercise you will define three Turtle graphics
#  functions, "draw_circles_for", "draw_circles_while"
#  and "draw_circles_recursive", each of which draws a set of
#  concentric circles centred on the screen's origin.  Each
#  function must accept the number of circles to be drawn as
#  its parameter.  So that the circles are all of different
#  sizes, global variable "separation" below should be used
#  to differentiate the radius of each successive circle.
#  The first circle should be of radius "separation" pixels,
#  the second of radius "2 * separation" pixels and so on.
#
#  This behaviour can be implemented easily using a FOR loop,
#  and with only a little more thought using a WHILE loop or
#  recursively.  Try doing it in all three ways.  The code
#  for drawing one circle can be common to all three
#  versions.
#

from turtle import *

# How much separation there should be between each successive
# circle's radius
separation = 10 # pixels

#---------------------------------------------------------

## DEVELOP YOUR THREE FUNCTIONS HERE
def draw_circles_for(how_many):
   for circle_num in range(1, how_many + 1):
      penup()
      radius = circle_num * separation
      goto(radius, 0)
      setheading(90)
      pendown()
      circle(radius)

def draw_circles_while(how_many):
   circle_num = 1
   while circle_num <= how_many:
      penup()
      radius = circle_num * separation
      goto(radius, 0)
      setheading(90)
      pendown()
      circle(radius)
      circle_num = circle_num + 1

def draw_circles_recursive(circle_num):
   if circle_num > 0:
      draw_circles_recursive(circle_num - 1)
      penup()
      radius = circle_num * separation
      goto(radius, 0)
      setheading(90)
      pendown()
      circle(radius)

#---------------------------------------------------------
#
# This main program calls one of your functions.  Uncomment
# the appropriate call for the function you are developing.
#

# Set up
setup()
title("Concentric circles")
speed("fastest")

# Test the functions by drawing 30 circles.
# Uncomment these calls one at a time to test your functions.
#
##draw_circles_for(30)
draw_circles_while(30)
# draw_circles_recursive(30)

# Clean up
hideturtle()
done()


