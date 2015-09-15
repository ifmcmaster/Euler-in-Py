# The trick here is to inclue a table of previous calculated counts.
# If we build a table of counts from the ground up, every time
# the number being tested falls below its base (its original state),
# the counts will already have been calculated. For example:
# when 14 becomes 7 via rule 1, we will already have calculated
# the counts for 7.
#
# Additionally, we can skip a step when the number is odd,
# as rule 2 will make it even, which will invoke rule 1.
# Therefore, we build rule 1 into rule 2, and wait for the
# number to fall below its base.

largestCount = 1
largestBase = 1
counts = {1:1}

for base in xrange(2,1000000):

    n = base
    count = 0

    while not n < base:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = ((3 * n) + 1)/2
            count += 2

    count += counts[n]
    counts[base] = count

    if count > largestCount:
        largestCount = count
        largestBase = base
    
print largestBase, " :", largestCount
