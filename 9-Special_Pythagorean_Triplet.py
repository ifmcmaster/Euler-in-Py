# Brute Force
# There are a number of checks we can make
# to speed up number-crunching. 
# Wikipedia provides a list of general properties
# of Pythagorean triples, however only a few a implented:
# 'c' is of the form 4n + 1
# a * b * c % 60 == 0
# either 'a' or 'b' is odd, not both.

import math

def perfect_square(number):
    square = int(math.sqrt(number))
    if square * square == number:
        return True
    else:
        return False

def sixty_check(a,b,c):
    if (a * b * c) % 60 == 0:
        return True
    else:
        return False

def sum_check(a,b,c):
    if a + b + c == 1000:
        return True
    else:
        return False

def square_sum_check(a,b,c):
    if a*a + b*b == c*c:
        return True
    else:
        return False

c = 1
n = 1

while c < 1000:
    b = 4
    c = (4*n)+1
    while b < c:
        if b % 2 == 0:
            a = 3
        else:
            a = 4
        while a < b:
            if sixty_check(a,b,c):            
                if sum_check(a,b,c):
                    if square_sum_check(a,b,c):
                        print a*b*c
                        quit()
            a += 2
        b += 1
    n += 1

