# Brute Force Approach, self-explanatory.
def bruteForce():
    sumSquares = 0
    squareSums = 0

    for x in xrange(1,101):
        sumSquares += x*x

    for x in xrange(1,101):
        squareSums += x

    squareSums = squareSums * squareSums

    return squareSums - sumSquares


# Triangular Number Approach
# The sum of real numbers up to 'n' is given by:
# (n(n+1))/2
# We adapt this formula for the sum of squares and
# the square of sums, such that:
# sumSquares = 1/6 * n(n+1)(2n+1)
# squareSums = 1/4 * (n(n+1))^2

sumSquares = round(1.0/6 * 100*101*(2*100+1))
squareSums = round(1.0/4 * (100*(101))*(100*(101)))

print "Brute Force: ", bruteForce()
print "Summations: ", int(squareSums - sumSquares)
