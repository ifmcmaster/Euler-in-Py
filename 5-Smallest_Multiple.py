##
# Brute Force Approach.
#
# Check each number past 2520 (incremented by 20)
# to see if they divide evenly by the largest
# composite and prime numbers. (Eg, checking for
# modulo by 2 is unneeded,as 2 is a factor of 12).
##

def bruteForce():
    number = 2520
    check = [19,18,17,16,15,
             14,13,12,11,7]
         
    found = False

    while True:

        number += 20
    
        for x in check:
            if number % x == 0:
                found = True
            else:
                found = False
                break

        if found == True:
            return number

##
# Prime Factorization
#
# Obtain the largest count of each prime
# number between 1 and 20, then mulitply
# them together. We are essentially creating
# the answer's product of primes, via the
# fundamental theorem of arithmetic.
##
def primeFactorization(input):
    
    number = input
    factor = 2
    primeList = []

    while factor <= int(input/2):
        if number % factor == 0:
            primeList.append(factor)
            number = number / factor
        else:
            factor += 1

    if number == input:
        primeList.append(number)

    return primeList


primeCount = {2:0,3:0,5:0,7:0,9:0,11:0,13:0,17:0,19:0}
primes = primeCount.keys()
total = 1

for x in xrange(11,21):

    primeList = primeFactorization(x)

    for y in primes:
        while primeCount[y] < primeList.count(y):
            total *= y
            primeCount[y] += 1

print "Prime Factorization: ", total
print "Brute Force..."
print "Brute Force: ",  bruteForce()
