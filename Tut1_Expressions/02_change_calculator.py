# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E

Amount = 20 #dollars
Milk = 2 * 2.50 #dollars
MarsBars = 5 * 1.20 #dollars
Tablets = 3.50 #dollars


Change = Amount - (Milk + MarsBars + Tablets) #calculating change
print('You will receive $', Change, 'change')

