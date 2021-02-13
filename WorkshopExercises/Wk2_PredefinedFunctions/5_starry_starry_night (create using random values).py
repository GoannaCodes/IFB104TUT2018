# Starry, starry night
#
# This exercise gives us some practice at creating graphics
# using random values.
#
# THE PROBLEM
#
# Draw the night sky as a black field containing 200 randomly-
# positioned white "stars" (dots), each of a randomly-chosen size.
# (The most realistic effect is achieved if the difference in
# sizes is only small.)
#
# Use the following problem-solving strategy:
#
# 1. Set up a drawing window of a known size
#    with a black background
# 2. Make the pen colour white and set the drawing
#    speed to "fastest"
# 3. Lift up the pen (so that you don't draw lines
#    between the stars)
# 4. For each star in a range of 200:
#    a. Choose a random x-y coordinate (being careful
#       that it is not off the edge of the screen)
#    b. Choose a random star size
#    c. Go to the location chosen
#    d. Draw a star (dot) of the chosen size
# 5. Hide the cursor and release the drawing window
#
# Hint: This is much easier than it sounds.  If you're not sure
# how to get started, use the "shooting gallery" demonstration
# program from the lecture as a guide.
#
# Comment: Once you get this program working, try experimenting
# with variations, e.g., by randomly changing the stars'
# colours.
#

# Import the necessary functions
from turtle import *
from random import randint

#Define values
screen_size = 300 #pixels


#Set up screen size, title and colour
setup(screen_size, screen_size)
title("Starry Night Sky")
bgcolor('black')

#Set a random pen color and adjust drawing speed
colormode(255)
randomcolour = (randint(0, 255), randint(0, 255), randint(0, 225))
pencolor(randomcolour)
print(randomcolour)
speed('fastest')
penup()

#Draw the randomly-positioned stars (dots)

for star in range(200):
    #choose a random star size
    star_size = randint(1, 7) #pixels
    max_coord = (screen_size - star_size)
    #co-ordinates to draw star
    x_pos = randint(-max_coord, max_coord)
    y_pos = randint(-max_coord, max_coord)
    
    penup()
    goto(x_pos, y_pos)
    pendown()
    dot(star_size)

hideturtle()
done()
    

