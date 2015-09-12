# Two methods for carrying variables
# into next iteration.

total = 0
previous = 1
current = 2

while current < 4000000:

    if current % 2 == 0:
        total += current
    
    previous, current = current, current + previous

'''
    swap = current
    current = current + previous
    previous = swap
'''

print total
