# Relatively straight-forward. Compute the sum of divisors for
# all numbers up to the bound, and if the sum is greater than the
# number itself, append it to a list of abundant numbers. Each
# iteration, if an abundant number is found, that number is added
# to all previously found abundant numbers, with the results being
# marked. By the end, each number not marked up to the bound is 
# added together for the total. Unfortunately, I am unsure 
# how to speed up the addition of abundant numbers - it runs
# at O(n^2), which is massive given the amount of numbers found.

import math
import time

# If bounding by square root, each divisor
# found will have a corresponding pair that is
# 'n' / divisor. For instance, 2 is a divisor of 6,
# so 6/2=3 is a divisor of 6.
def sum_divisors(n):
	sum = 0
	for i in xrange(2, int(math.ceil(math.sqrt(n)))):
		if n % i == 0:
			sum += i
			pair = n / i
			if pair != i:
				sum += pair

	return sum

## Main ##
bound = 28124
totalSum = 0
abundantNums = []
sums = {}
start = time.time()

print "Creating dictionary for sums of abundant numbers..."
for i in xrange(bound):
	sums[i] = False;
print "Created: ", time.time() - start

print "Finding abundant numbers..."
for i in xrange(2,bound):

	# For benchmarking
	# if i % 1000 == 0:
	# 		print "	Reached: ", i 

	sd = sum_divisors(i)
	if sd > i:
		abundantNums.append(i)
		for x in abundantNums:
			if x + i > bound:
					break
			sums[x + i] = True

print "Abundant numbers found: ", time.time() - start

print "Computing sums..."
for i in xrange(bound):
	if sums[i] == False:
		totalSum += i

print "Completed: " , time.time() - start
print totalSum