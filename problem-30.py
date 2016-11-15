def digits_sum_power(number,power):
	digits_sum = 0
	for i in str(number):
		digits_sum += int(i)**power
	return digits_sum

total = 0

for i in range(2,1000000):
	if i == digits_sum_power(i,5):
		total += i

print( total )