# Through use of the modulo operator,
# we are able to cherry pick multiples
# of 3 and 5.

total = 0

for x in xrange(0,1000):
    if x % 3 == 0 or x % 5 == 0:
        total += x

print total
