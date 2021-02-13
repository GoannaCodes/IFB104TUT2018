#---------------------------------------------------------------------
#
# Solar system
#
# Space is big. Really big. For we mere mortals it's often hard to
# visualise the immensity of the objects in the heavens.  In this
# exercise we'll try to get an understanding of the relative sizes
# of some of the planets in our solar system, by drawing dots
# representing them all to the same scale.
#
# Below are two lists containing data about some planets in our
# solar system.  Your task is to draw a dot of the suggested colour
# and diameter for each of the planets using Turtle's
# "dot" method.  In between drawing each dot you should move
# the cursor to a different location on the screen so that the
# dots are not all on top of one another.
#
# Optionally, you can also choose to write the planet's name next
# to it, using Turtle's "write" method.  You can change the colour
# of the text displayed using Turtle's "color" method.  To change
# the font size, e.g., to 12, call the "write" method with the
# argument "font=('size=12')".
#
# Importantly, you should not "hardwire" the colours and diameters
# in your code.  You should instead refer to the appropriate list
# element by its index, so that your program can draw different
# planets simply by changing the data in the lists.

from turtle import *

# Lists of data your code should refer to
name = ['Mars', 'Earth', 'Neptune', 'Venus', 'Jupiter']
diameter = [13.6, 25.6, 97.2, 24.2, 285.6] # each pixel represents 500km
colour = ['red', 'light blue', 'light grey', 'yellow', 'tan']

# Create a canvas representing the vast emptiness of space
setup()
title('Some planets in our solar system')
bgcolor('black')
penup() # we can draw dots with the pen up

#Set position of turtle to draw Mars
setheading(180) #turn to face west
forward(300) #move forward 300 pixels
#####################################################################

#Start drawing Mars
pendown()
pencolor(colour[0]) #setting pen color to first entry in colour list
dot(diameter[0]) #draw dot with first entry's diameter in diameter list
penup() #stop drawing

#Setting position for writing planet name
setheading(270) #turn to face south
forward(diameter[0] + 10) #move cursor below planet
write('Mars', 12) #write planet name with size 12 font

#Move position for next planet
home() #go back to center of screen
setheading(180) #turn to face west
forward(275 - (diameter[0] * 2)) #move distance away from previously drawn planet

#####################################################################

#Start drawing Earth
pendown()
pencolor(colour[1]) #setting pen color to second entry in colour list
dot(diameter[1]) #draw dot with second entry's diameter in diameter list
penup() #stop drawing

#Setting position for writing planet name
setheading(270) #turn to face south
forward(diameter[1] + 10) #move cursor below planet
write('Earth', 12) #write planet name with size 12 font

#Move position for next planet
home() #go back to center of screen
setheading(180) #turn to face west
forward(250 - diameter[2]) #move distance away from previously drawn planet

#######################################################################

#Start drawing Neptune
pendown()
pencolor(colour[2])
dot(diameter[2])
penup()

#Setting position for writing planet name
setheading(270)
forward((diameter[2]/2) + 20)
write('Neptune', 12) 

#Move position for next planet
home()
setheading(180)
forward(250 - diameter[2] * 2)

#######################################################################

#Start drawing Venus
pendown()
pencolor(colour[3])
dot(diameter[3])
penup()

#Setting position for writing planet name
setheading(270)
forward(diameter[3] + 10)
write('Venus', 12)

#Move position for last planet
home()
setheading(0)
forward(diameter[4]/2)

#Start drawing Jupiter
pendown()
pencolor(colour[4])
dot(diameter[4])
penup()

#Setting position for writing planet name
setheading(270)
forward(diameter[4]/2 + 30)
write('Jupiter', 12)


# Exit gracefully
hideturtle()
done()

