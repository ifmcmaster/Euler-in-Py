# Brute force. A lot of improvements can be made 
# with prior knowledge (only brute-forcing numbers
# greater than 900, for example).

palindromes = []
largestPalindrome = 0

for x in xrange(100,1000):
    for y in xrange(100,1000):
        check = x * y
        if str(check) == str(check)[::-1]:
            if check > largestPalindrome:
                largestPalindrome = check

print largestPalindrome
