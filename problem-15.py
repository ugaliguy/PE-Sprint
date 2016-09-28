# Python 3

# Find the number of paths from top left to bottom right corners 
# on an m X n grid. Answer is (m+n)Cm = (m+n)Cn.

def choose(n,k):
	if (n < k) or (k < 0) or (n < 0):
		return 0
	else:
		numerator = 1
		denominator = 1
		for i in range(1, min(k, n - k) + 1):
			numerator *= n
			denominator *= i
			n -= 1
		return numerator//denominator

print( choose(40,20)) # answer is 137846528820
