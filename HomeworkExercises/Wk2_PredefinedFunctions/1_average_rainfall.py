# Highest average rainfall
#
# THE PROBLEM
#
# This exercise tests your ability to use lists in Python.
# Assume the following values have already been entered into the
# Python interpreter, denoting the rainfall in millimetres recorded
# for several Queensland towns over a one month period.  No
# record was made for days when it didn't rain, so each of the
# lists is of a different length.

aurukun =  [15, 9, 11, 4, 10, 20, 95] #164//7 
burdekin = [13, 9, 5, 80, 150, 145] #402//6 = 67
cardwell = [115, 90, 100, 46, 130, 200, 195, 10, 3, 8] #897//10
daintree = [140, 120, 110, 53, 100, 50, 175] #748/7 = 107
tully =    [115, 90, 100, 130, 200, 195] #830//6 = 138

# Write code to calculate the highest average rainfall
# and print the result in a meaningful message to the screen.
#
# HINTS:
# * Use the following built-in functions: sum, len and max.
# * Your task is to find the highest average rainfall - NOT the
#   town with the highest average rainfall.
# * The correct answer is 138mm.

print('The rainfall of several Queensland towns were recorded over a month period.')
#calculate average rainfall of aurukun
auru = sum(aurukun)//len(aurukun)
#print('Average rainfall of Aurukun was', auru, 'milimetres')

#calculate average rainfall of burdekin
burd = sum(burdekin)//len(burdekin)
#print('Average rainfall of Burdekin was', burd, 'milimetres')

#calculate average rainfall of cardwell
card = sum(cardwell)//len(cardwell)
#print('Average rainfall of Cardwell was', card, 'milimetres')

#calculate average rainfall of daintree
dain = sum(daintree)//len(daintree)
#print('Average rainfall of Daintree was', dain, 'milimetres')

#calculate average rainfall of tully
tul = sum(tully)//len(tully)
#print('Average rainfall of Tully was', tul, 'milimetres')

avg = max(auru, burd, card, dain, tul)
print('Highest average rainfall was', avg, 'milimetres')
