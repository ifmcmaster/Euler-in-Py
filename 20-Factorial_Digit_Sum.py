# Like problem 13, this factorial isn't a problem
# for built in functions to handle. A proper
# solution would be pulling the last digits
# off with a % 10 and adding that to the
# total sum, but strings are used for fun.

import math
fact = math.factorial

sum = 0
n = str(fact(100))
for x in n:
    sum += int(x)

print sum

