# Python 3

a = 1
b = 0
n = 1

while( len(str(a))  < 1000 ):
	dummy = a
	a += b
	b = dummy
	n += 1
	
print("%d has 1000 digits, n = %d" % (a, n)) 
# F_4782 is the first Fibonacci number with 1000 digits
