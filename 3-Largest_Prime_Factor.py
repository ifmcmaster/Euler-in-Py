# The algorithm used here is based off the 
# prime factorization algorithm provided in
# Discrete Mathematics for Computer Science 
# by Jenkyns/Stephenson.
#
# Only the largest result is printed.

import math

input = 600851475143
maxNumber = int(math.sqrt(input))
primeFactors = []

for x in xrange(2, maxNumber):
    while input % x == 0:
        primeFactors.append(x)
        input = input / x

print primeFactors[-1]
