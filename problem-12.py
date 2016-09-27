# Python 3

import math

# First number to have 500 divisors
c = (2**4)*(3**4)*(5**4)*7*11

# Function to calculate the number of divisors of integer n
def num_divisors(n):
    bound = int(math.sqrt(n))
    divisors = []
    for i in range(1, bound+1, 1):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n/i)
    return len(divisors)
                
# An integer is triangular iff 1+8*n is a perfect square
def is_triangular(n):
    return int(math.sqrt(1+8*n)) - math.sqrt(1+8*n) == 0
    
# print(is_triangular(28))

# Function to calculate the last term of the series adding up to the triangle number    
def last_term(n):
    if is_triangular(n):
        return int((-1 + math.sqrt(1+8*n))/2)
    else:
        return None
        
# print(last_term(28))

# Starting from c, iterate sequentially checking for the next triangle number
while not is_triangular(c):
    c += 1

# Calculate the last term of the series that adds up to 
# the newly calculated triangle number c
lt = last_term(c)

# Iterate over triangle numbers checking for number of divisors > 500
while num_divisors(c) <= 500:
    # add the next term to c to get the next triangle number
    c += (lt + 1)
    lt += 1
print( c )
        