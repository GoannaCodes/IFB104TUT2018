
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no: N10269142
#  Student name: Anna Nguyen
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#Use the turtle program to replicate a drawing of 4 overlapping circles
#of different colours.The drawing your code creates should contain
#the same number of shapes, have the same fill colours
#(yellow, green, blue and red) and outline colour (black),and overlap
#in the same fashion. The produced drawing from the program must not
#contain elements that are not represented in the given drawing
#(connecting lines).


#import everything from turtle module
from turtle import *

#set up canvas
setup()
title('Overlapping circles') #set title of canvas
pencolor('black') #set pencolor to black
width(3) #set width of pen to 3

#define function to draw a circle
def circ(color, radius = 55):
    #draw circle
    penup() #don't start drawing yet
    fillcolor(color) #set filling to given color
    setheading(180) #turtle facing west
    pendown() #start drawing
    begin_fill() #start filling in space
    circle(radius) #draw a circle with radius 50
    penup() #stop drawing
    end_fill() #stop filling in space

    #set position for next circle
    forward(radius - 10) #move forward(left) by the given radius - 10 pixels
    setheading(270) #turtle now facing south
    forward(radius/2 + 10) #move forward(down) by given radius + 10 pixels

#draw circles by calling function
circ('red') #set parameter of color to red for function circ
circ('blue') #set parameter of color to blue for function circ
circ('lime') #set parameter of color to lime for function circ
circ('yellow') #set parameter of color to yellow for function circ

#tidy up
hideturtle() #hide turtle cursor
done() 


