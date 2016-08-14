# Python 3

# This is very ineffcient

def collatz_length(n):
    # 0 and 1 return self as length
    if n <= 1: return n
 
    length = 1
    while (n != 1):
      if (n % 2 == 0):
        n = n/2
      else:
        n = 3*n + 1
       
      length += 1
     
    return length
    
start = 1
longest = 0

for x in range(1, 1000001):
    c_len = collatz_length(x)
    if c_len > longest:
    	start = x
    	longest = c_len
    	
print("The longest chain has length " + str(longest) + " and starts with " + str(start))

# The longest chain has length 525 and starts with 837799