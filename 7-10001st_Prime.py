# Finding primes is always a brute force
# approach, but can be improved upon in a
# variety of ways. This method uses a
# sieve, which are unruly for this type
# of problem unless an upper-bound is 
# specified. We can obtain a bound with
# the prime number theorem, p ~= nlg(n).
# 10001*lg(10001) ~= 132000, so 150000
# is used for safety.

import math

primes = []
bound = 150000

# Initialize Sieve
numberList = []
for x in xrange(bound):
    numberList.append(True)

# Determine Primes in Sieve
for i in xrange(2,bound):
    if numberList[i]:
        j = i * i 
        while j < bound:
            numberList[j] = False
            j += i

# Create a list consisting purely
# of primes, and use index for answer.
for i in xrange(2, bound):
    if numberList[i] == True:
        primes.append(i)

print primes[10001 - 1] 
