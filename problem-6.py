# Python 3

# I feel like the accepted answer is the opposite of what was asked for.


n = 100

def sum_of_squares(n):
	result = n*(n+1)*(2*n+1)/6
	return result
	
def square_of_sum(n):
	result = (n*(n+1)/2)**2
	return result
	
answer = sum_of_squares(n) - square_of_sum(n)

print(answer) 
