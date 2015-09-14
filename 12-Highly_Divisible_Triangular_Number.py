# It is unlikely one will brute force this problem 
# within 1 minute using Python unless optimizations
# are made.
#
# The trick to this problem, like problem 5, is
# understanding the Fundamental Theorem of Arithmetic:
# each integer is composed of a unique product of primes.
#
# Triangle Numbers are defined by equation:
# (n * (n + 1))/2
#
# By breaking up this equation, we can compute
# the prime factorization or two smaller numbers,
# then combine their factors to create a larger number.
# This is faster than computing prime factorizations
# for large numbers.
#
# Factor counts are generated from the prime factors 
# of a number using the formula (m + 1)(n + 1)(p + 1)...

from collections import Counter
import math
import time

def prime_factorization(input):
    
    number = input
    factor = 2
    primeList = []

    while factor <= int(math.sqrt(input)):
        if number % factor == 0:
            primeList.append(factor)
            number = number / factor
        else:
            factor += 1

    if number == input:
        primeList.append(number)

    return primeList

# This function obtains the counts of each prime number 
# in a given list of primes, then computes the factor count.
def get_factor_count(input):
    factorCount = 1
    for x in Counter(input).values():
        factorCount *= (x + 1)          # The formula described above.
    return factorCount


triangleNumber = 0
n = 1

while True:

    triangleNumber += n
    factorCount = 0

    # Here we break up the Triangle Number equation.
    # If the number is odd, we cannot use n/2, as that
    # will result in a fraction, so (n+1)/2 must be used.
    # Notice that multiplying the arguments results in the
    # equation.
    if n % 2 == 0:
        primes1 = prime_factorization(n/2)
        primes2 = prime_factorization(n+1)
    else:
        primes1 = prime_factorization(n)
        primes2 = prime_factorization((n+1)/2)

    factorCount = get_factor_count(primes1 + primes2)

    if factorCount > 500:
        print triangleNumber
        print "Factor Counct: ", factorCount
        print time.time() - s
        break

    n += 1
