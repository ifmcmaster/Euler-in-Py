# Sieve method is used.
# Problem 7 explains the sieve.

numberList = []
bound = 2000000
sum = 0

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

for x in xrange(2,bound):
    if numberList[x] == True:
        sum += x

print sum
