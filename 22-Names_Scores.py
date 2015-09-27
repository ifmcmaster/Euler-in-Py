# Brute Force is near instantenous on a relatively slow machine.
# If there is a more elegant solution, it is unneeded here.

import re
letterScores = {'"':0}	# I included " in the names during evaluation.

totalSum = 0

# Assings scores to each letter via ASCII table
for i in xrange(1,27):
	letterScores[chr(i + 64)] = i

with open('p022_names.txt','r') as input:
	names = re.split(',', input.read())
	names.sort()
	for i in xrange(len(names)):
		sum = 0
		for char in names[i]:
			sum += letterScores[char]
		sum *= i+1
		totalSum += sum

print totalSum