# Days calculator
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the number of days in each
# month of a given (non-leap) year.

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

# PART 1
#
# Write an expression, or expressions, to calculate the number of days
# in each quarter (three month period) of the year, using the values
# introduced above, and print the result.
quarter1 = january + february + march
quarter2 = april + may + june
quarter3 = july + august + september
quarter4 = october + november + december

print('The number of days in each quarter of the year are', quarter1, quarter2, quarter3, quarter4, 'days respectively')

# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.
firsthalf = quarter1 + quarter2
secondhalf = quarter3 + quarter4

print('There is ', firsthalf, 'days in the first half of the year and ', secondhalf, 'days in the second half')


# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.

total_days = firsthalf + secondhalf
print('There are', total_days, 'days in the year')

