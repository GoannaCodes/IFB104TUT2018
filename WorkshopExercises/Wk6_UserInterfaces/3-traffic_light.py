#----------------------------------------------------------------
#
# TRAFFIC LIGHT
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a drawing canvas and three buttons.
# Each time one of the buttons is pressed a red, yellow
# or green circle should be drawn on the canvas, in
# imitation of a traffic light.
#
# As an additional feature, you could restrict the
# buttons so that the lights can only follow the usual
# green-yellow-red-green sequencing.  (There is no yellow
# between red and green in real traffic lights!)
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Canvas

# Create a window
traffic_window = Tk()

# Give the window a title
traffic_window.title('Traffic Light')


###### PUT YOUR CODE HERE

# 1. Define functions to be called when one of the buttons
#    is pressed which will create appropriately coloured
#    ovals on the drawing canvas, using the "create_oval"
#    "Canvas" method with an appropriate "fill" colour
#    parameter
def red_light():
    Light.create_oval(50, 50, 100, 100, fill = "red")
def yellow_light():
    Light.create_oval(50, 50, 100, 100, fill = "yellow")
def green_light():
    Light.create_oval(50, 50, 100, 100, fill = "green")
    
# 2. Create the three Button widgets and pack them into
#    the main window
Red = Button(traffic_window, text = "Red",
             font = ("Arial", 15), command = red_light)
Red.grid(row = 0, column = 1)

Yellow = Button(traffic_window, text = "Yellow",
                font = ("Arial", 15), command = yellow_light)
Yellow.grid(row = 0, column = 2)

Green = Button(traffic_window, text = "Green",
               font = ("Arial", 15), command = green_light)
Green.grid(row = 0, column = 3)
# 3. Create the drawing Canvas widget and pack it into the
#    main window
Light = Canvas(traffic_window, width = 190, height = 150)
Light.grid(row = 1, column = 2, columnspan = 2)

# Start the event loop to react to user inputs
traffic_window.mainloop()
