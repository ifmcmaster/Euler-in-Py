# This problem is easily solvable using combinatorics.
# The answer can be found with the formula:
# (x + y) choose [x or y]
# as in the example provided:
# (2 + 2) choose 2 = 6
#
# So, our answer is:
# 40 choose 20 
#
# We must move exactly 20 steps to the right and
# 20 steps down in order to reach the right bottom corner.
#
# That is 40 steps total. 
#
# Now assume you move in a straight line to the right.
# You have the option to choose at which point you will
# turn down, but you must do so 20 times.
#
# You are choosing 20 spots to turn at.
# This gives us the mentioned formula.
# 
# To find "n choose k", we use the "binomial coefficient" formula.

import math
fact = math.factorial

x = 20
y = 20

# The formula for binomial coefficients is:
# (n!)/(k! * (n - k)!)
def binomial_coefficient(n, k):
    return fact(n)/(fact(k) * fact(n - k))

print binomial_coefficient(x+ y, y)
