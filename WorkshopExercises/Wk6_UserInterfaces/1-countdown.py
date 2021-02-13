#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which some other value can be
# displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')


##### PUT YOUR CODE HERE
Label_value = 10
# 1. Define a function to be called when the button is
#    pressed which will change the label's value

#Back end function
def count_down():
    global Label_value
    if Label_value == 1:
        Number["text"] = "Go!"
    else:
        Label_value = Label_value - 1
        Number["text"] = str(Label_value)
       
# 2. Define the Button widget and pack it into the
#    main window
start_button = Button(countdown_window, text = "Press me!",
                      font = ('Arial', 25), command = count_down)
start_button.pack()

# 3. Define the Label widget and pack it into the main
#    window
Number = Label(countdown_window, text = str(Label_value), font = ('Arial', 25))
Number.pack()

# Start the event loop to react to user inputs
countdown_window.mainloop()
