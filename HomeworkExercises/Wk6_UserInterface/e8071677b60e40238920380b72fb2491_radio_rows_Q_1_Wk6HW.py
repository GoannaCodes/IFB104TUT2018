#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no: 10269142
#  Student name: Anna Nguyen
#
#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
#
# 10 labels, 2 radio buttons (as per diagram)
# Initially, all Labels are displayed in grey.
# When one of the Radiobuttons is selected by the user, the corresponding
# row of labels changes colour:
# When Row 1 is selected, the first row of labels changes to yellow
# (and the other row is grey).
# When Row 2 is selected, the second row of labels changes to red
# (and the other row is grey).

#--------------------------------------------------------------------#

#
# Import the Tkinter functions
from tkinter import *

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Show Rows')

# PUT YOUR CODE HERE-------------------------------------------------#  
#Variable to determine whether radio button is selected
label_colour = IntVar()

#Function to change colour of label's when radio button is selected
def change_colour():
   if label_colour.get() == 1:
      #Change background to active background
      R0C1["state"] = ACTIVE
      R0C2["state"] = ACTIVE
      R0C3["state"] = ACTIVE
      R0C4["state"] = ACTIVE
      R0C5["state"] = ACTIVE

      #Set other row to default background
      R1C1["state"] = NORMAL
      R1C2["state"] = NORMAL
      R1C3["state"] = NORMAL
      R1C4["state"] = NORMAL
      R1C5["state"] = NORMAL
   else:
      #Change background to active background
      R1C1["state"] = ACTIVE
      R1C2["state"] = ACTIVE
      R1C3["state"] = ACTIVE
      R1C4["state"] = ACTIVE
      R1C5["state"] = ACTIVE

      #Set other row to default background
      R0C1["state"] = NORMAL
      R0C2["state"] = NORMAL
      R0C3["state"] = NORMAL
      R0C4["state"] = NORMAL
      R0C5["state"] = NORMAL

#Create Radio button widgets
first_radio_button = Radiobutton(the_window, text = 'Row 1',
                                 variable = label_colour, value = 1,
                                 command = change_colour)
second_radio_button = Radiobutton(the_window, text = 'Row 2',
                                  variable = label_colour, value = 2,
                                  command = change_colour)

#Create labels with background and activebackground settings
#Label properties for row 1 radio button
R0C1 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Yellow", state = NORMAL)
R0C2 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Yellow", state = NORMAL)
R0C3 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Yellow", state = NORMAL)
R0C4 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Yellow", state = NORMAL)
R0C5 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Yellow", state = NORMAL)

#Label properties for row 2 radio button
R1C1 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Red", state = NORMAL) 
R1C2 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Red", state = NORMAL)  
R1C3 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Red", state = NORMAL)
R1C4 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Red", state = NORMAL)
R1C5 = Label(the_window, bg = "Grey", width = 5,
             borderwidth = 1, relief = "solid",
             activebackground = "Red", state = NORMAL)
       

#Place widgets onto window
first_radio_button.grid(row = 0, column = 0)
second_radio_button.grid(row = 1, column = 0)

R0C1.grid(row = 0, column = 1, padx = 2)
R0C2.grid(row = 0, column = 2, padx = 2)
R0C3.grid(row = 0, column = 3, padx = 2)
R0C4 .grid(row = 0, column = 4, padx = 2)
R0C5.grid(row = 0, column = 5, padx = 2)

R1C1.grid(row = 1, column = 1, padx = 2)
R1C2.grid(row = 1, column = 2, padx = 2)
R1C3.grid(row = 1, column = 3, padx = 2)
R1C4.grid(row = 1, column = 4, padx = 2)
R1C5.grid(row = 1, column = 5, padx = 2)
#----------------------------------------------------------------

# Start the event loop to react to user inputs
the_window.mainloop()
