# Python 3

# Find the sum of the digits of 2^1000

big = 2**1000
s = list(str(big))

total = 0
for i in s:
	total += int(i)
	
print(total)