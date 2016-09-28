# Python 3

alpha = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 
9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 
40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

total = 0
for i in range(1,1001):
	if i <= 20:
		total += len(alpha[i])
	elif i <= 99:
		total += (len(alpha[(i//10)*10]) + len(alpha[i%10]))
	elif i <= 999:
		hundreds = i//100 # Gives the hundreds digit
		rem = i%100
		if rem == 0:
			total += (len(alpha[hundreds]) + len('hundred'))
		elif rem <= 20:
			total += (len(alpha[hundreds]) + len('hundred') + len('and') + len(alpha[rem]))
		else:
			total += (len(alpha[hundreds]) + len('hundred') + len('and') 
			+ len(alpha[(rem//10)*10]) + len(alpha[rem%10]))
	else:
		total += (len(alpha[1]) + len('thousand'))
		
print( total )
	