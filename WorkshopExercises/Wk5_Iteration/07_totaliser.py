#----------------------------------------------------------------
#
# Totaliser
#
# Develop a program which repeatedly prompts the user to
# enter a number.  For each number entered, the program
# should print a message showing the sum of all
# the numbers entered so far.
#
# The program should stop when the word 'stop' is entered
# instead of a number.
#
# For instance, the program's interaction with the user
# should look something like the following.
#
#   Please enter a number or "stop": 5
#   The total so far is 5
#   Please enter a number or "stop": 6
#   The total so far is 11
#   Please enter a number or "stop": 3
#   The total so far is 14
#   Please enter a number or "stop": stop
#
# Hint: You will need to use Python's "input" function
# to read what the user types as a string, and its "eval"
# function to turn numbers entered by the user from strings
# to integers.
#


#----------------------------------------------------------------
#
# An interactive program which repeatedly prompts the
# user to enter a number and for each one entered shows the
# sum of all the numbers entered so far, until string 'stop'
# is entered
#

##### DEVELOP YOUR INTERACTIVE PROGRAM HERE
total = 0
user_number = input('Please enter a number or "stop": ')
while user_number != "stop":
   total = total + eval(user_number)
   print('The total so far is ' + str(total))
   user_number = input('Please enter a number or "stop": ')



