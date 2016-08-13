# Python 3

# Note that 999**2 == 998001
# Find a more efficient method if possible.

def is_palindrome(n):
	sn = str(n)
	if sn == sn[::-1]:
		return True
	else:
		return False

def find_largest_palindrome():
	pal = -1
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			if i*j > pal and is_palindrome(i*j):
				pal = i*j
	return pal
	
print(find_largest_palindrome())