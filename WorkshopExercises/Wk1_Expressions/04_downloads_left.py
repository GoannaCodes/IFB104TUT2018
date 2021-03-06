# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

track_cost = 120 # cost in cents for downloading one track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
#convert track_cost to dollars (different units)
track_cost = 1.20 #dollars
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
Spent = num_downloaded * track_cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
Balance = budget - Spent
# 3. Divide the balance left by the track cost to a whole number
Tracks = Balance//track_cost
# 4. Print the number of tracks left
print('Can afford to download', Tracks, 'tracks')

# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

