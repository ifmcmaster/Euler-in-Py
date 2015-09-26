# We need to get the divisors for each number under 10000.
# Rather than manually test all numbers < n as divisors of n,
# we can generate primes via sieve, then test those instead.
# So, we generate primes under 10000 (a bound of 5000 is used,
# but can be modified for 100), then for each number < 10000,
# we get its prime composition through modulo operation against
# each prime from the sieve. We use that composition to generate
# the divisors through combinatorics, then finally get the
# sum of the divisors for n. If we nest that function within
# itself, we can do the final amicaple number check.
# (The nesting will make sense once seen.)


import math
import itertools


# Generate Primes from sieve
def sieve(bound):
    primes = []
    bound = bound/2

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

    return primes

# Get prime factors by testing against sieve
def prime_factorization(n, primes):
    number = n
    factors = []

    for prime in primes:
        number = n
        if number % prime == 0:
            factors.append(prime)
            number /= prime
            while(number % prime == 0):
                factors.append(prime)
                number /= prime

    return factors

# Get divisors through combinatorics.
# Every prime needs to be multiplied
# together in every possible way.
def compute_divisors(primeFactors):
    divisors = [1]
    factorCount = len(primeFactors)

    for i in xrange(1,factorCount):
        for tuple in itertools.combinations(primeFactors, i):
            result = reduce(lambda x, y: x*y, tuple)
            divisors.append(result)
    

    divisors = sorted(list(set(divisors)))

    return divisors

# Self-explanatory
def sum_divisors(n,primes):
    divisors = compute_divisors(prime_factorization(n,primes))
    return reduce(lambda x,y: x+y, divisors)


## Main ##
primes = sieve(10000)

amicableNumbers = []
for i in xrange(1,10000):
    num1 = sum_divisors(i,primes)
    if i == num1: # (6 and 28 are amicaple with themselves)
        continue
    num2 = sum_divisors(num1,primes) # The nested function
    if i == num2:
        pair = sorted([num1,num2])
        if pair not in amicableNumbers:
            amicableNumbers.append(pair)


sumTotal = 0
for pair in amicableNumbers:
    for number in pair:
        sumTotal += number

print sumTotal