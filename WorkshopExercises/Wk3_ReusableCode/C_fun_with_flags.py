#--------------------------------------------------------------------
#
# Fun With Flags
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# accompanying this file you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

#define global constants
flag_width = 600
flag_height = 400
stripe_height = 80

# Set up the drawing environment
setup(600, 400)
setworldcoordinates(0, 0, flag_width, flag_height) #make (0, 0) to bottom-left corner

#draw green and yellow stripes for togo flag
penup() #don't start drawing yet
goto(0, stripe_height)
setheading(90) #point north
for strip_num in range(2):
    stripe(flag_width, stripe_height, "green")
    forward(stripe_height)
    stripe(flag_width, stripe_height, "yellow")
    forward(stripe_height)
#draw one more green stripe
    stripe(flag_width, stripe_height, "green")

#draw union
    
# Exit gracefully
hideturtle()
done()
