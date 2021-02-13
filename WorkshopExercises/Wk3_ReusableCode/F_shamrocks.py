#----------------------------------------------------------------------
#  Luck of the Irish
#
#  As another example of code reuse, in this exercise you will develop
#  a Turtle graphics function to draw a shamrock (a three-leaf clover)
#  and use it to populate an Irish field.
#

# Import the turtle graphics functions
from turtle import *

# Set up the "grassy field"
field_size = 600 # pixels
setup(field_size, field_size)
bgcolor("dark green")
title("Luck of the Irish")

# Adjust the drawing speed, if necessary
speed('normal')


#----------
# Step 1
#
# Define a function that draws a single shamrock.  It should have
# two parameters, the x and y coordinates at which to draw the
# image.  The shamrock should consist of three circular leaves and
# a stem.  Choose an appropriate colour, distinct from the background.

#define function to draw a single shamrock
def shamrock(x_coord, y_coord):
    fillcolor('green')
    pencolor('sea green')
    for leaf in range(3):
        goto(15 + x_coord, y_coord)
        setheading(180) #start drawing from westmost point of leaf
        begin_fill()
        circle(15) #draw a circle of radius 15
        end_fill()

        #position for right leaf
        
    

#----------
# Step 2
#
# Write a main program to display 50 (or so) shamrocks randomly
# positioned on the field.  Use the field size defined above
# to limit the placement of shamrocks.

### PUT YOUR MAIN PROGRAM HERE
from turtle import *

goto(15 + 0, 0)
setheading(180) #start drawing from westmost point of leaf
begin_fill()
circle(15) #draw a circle of radius 15
end_fill()

# Exit gracefully
hideturtle()
done()
