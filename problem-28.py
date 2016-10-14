# Python 3

def sum_diag(n):
	if n == 0:
		return 1
	else:
		return 4*(2*n + 1)**2 - 12*n + sum_diag(n-1)
		
print(sum_diag(n))

# When n = 500, answer is 669171001
