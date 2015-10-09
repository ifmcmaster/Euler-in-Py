# Not a challenge if you use built in combinatoric libraries!
# The challenge probably intends one to implement their own
# permutation function. I might include this at a later time.

import itertools

counter = 1

for i in itertools.permutations('0123456789'):
	if counter == 1000000:
		print ''.join(i)
		break
	counter += 1