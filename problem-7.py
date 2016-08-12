# Python 3

# Find a more efficient way to do this
# Try the Sieve of Eratosthenes

def is_prime(n):
	if n == 1:
		return False
	elif n > 2 and n%2 == 0:
		return False
	else:
		for i in range(3, int(n**0.5)+1, 2):
			if n%i == 0:
				return False
	return True

nth = 1
p = 1
while nth != 10001:
	p += 2
	if is_prime(p):
		nth += 1
		
print(p)