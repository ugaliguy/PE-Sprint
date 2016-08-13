# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143
last_factor = 1
# Use the fact that no prime divisor can exceed square-root of n
r = math.sqrt(n)
largest_factor = math.floor(r)

# First find the largest power of 2 that divides n
if n%2 == 0:
	last_factor = 2
	n /= 2
	while n%2 == 0:
		n /= 2
else:
	last_factor = 1

# Now we are left with an odd integer
factor = 3
while n > 1 and factor <= largest_factor:
	if n%factor == 0:
		n /= factor
		last_factor = factor
		while n%factor == 0:
			n /= factor

		largest_factor = math.sqrt(n)
	factor += 2

if n == 1:
	print(last_factor)
else:
	print(n)