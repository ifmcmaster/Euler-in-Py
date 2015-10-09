# The only special trick here is using logarithms to compute
# the length of a number. This is a basic trick in discrete
# mathematics, and is more typically used to determine the number
# of bits needed to represend a binary number, in which log base 2
# is used.

import math
import time

counter = 2
last = 1
n = 1

start = time.time()
while int(math.log(n,10))+1 != 1000:
	temp = n
	n = last + n
	last = temp
	counter += 1

print "Completed: ", time.time() - start
print counter
