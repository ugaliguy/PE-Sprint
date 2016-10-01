# Python 3

import math

n = 100
digits = list(str(math.factorial(n)))

total = 0
for d in digits:
	total += int(d)
	
print( total )
