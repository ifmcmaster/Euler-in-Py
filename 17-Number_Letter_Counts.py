# Straight-forward.
# The hardest part here is ensuring your spellings are correct.


lowCount = ["","one","two","three","four","five","six",
            "seven","eight","nine","ten","eleven","twelve",
            "thirteen","fourteen","fifteen","sixteen",
            "seventeen","eighteen","nineteen"]
highCount = ["zeroty","tenty","twenty","thirty","forty",
             "fifty","sixty","seventy", "eighty", "ninety"]

hundred = 7                 # length of "hundred"

sum = len("onethousand")    # including 1000 simplifies the loop

for x in xrange(1,1000):
    
    flatHundred = False     # one hundred vs one hundred 'AND' one

    n = x % 100
    if n != 0:
        if n < 20:
            sum += len(lowCount[n])
        else:
            digits = str(n)
            tens = len(highCount[int(digits[0])])
            ones = len(lowCount[int(digits[1])])
            sum += tens + ones

    else:
        flatHundred = True

    x /= 100
    if x > 0:
        sum += len(lowCount[x]) + hundred 
        if not flatHundred:
            sum += 3 # for "and"
            print "    and = 3"

print sum
