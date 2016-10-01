# Python 3

def divisor_sum(n): # Returns sum of proper divisors of n
	s = 1
	for i in range(2,n):
		if n%i == 0:
			s += i
	return s
	
def amicable_pairs_sum(bound):
	total = 0
	for i in range(1, bound):
		if divisor_sum(divisor_sum(i)) == i and i < divisor_sum(i):
			total += (i + divisor_sum(i))
	return total
	
print( amicable_pairs_sum(10000) )