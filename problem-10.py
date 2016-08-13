# Python 3

# Summation of primes

import math

def sum_primes(upper):
	sieve = list(range(upper + 1))
	sieve[1] = 0
	for n in range(2, int(math.sqrt(upper)) + 1):
		if sieve[n] > 0:
			for i in range(n**2, upper + 1, n):
				sieve[i] = 0
	return sum(sieve)
	
print(sum_primes(2000000))  # 142913828922