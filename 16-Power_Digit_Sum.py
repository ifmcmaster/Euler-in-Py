# This can be written in as little as one line of code
# using through using strings instead of numbers,
# but in the spirit of having a take-away, here
# is how you pull individual digits off a number.

def sum_digits(n):
    sum = 0
    
    while n > 0:
        sum += n % 10
        n /= 10

    return sum

print sum_digits(2**1000)
