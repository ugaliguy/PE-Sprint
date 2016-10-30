# Python 3

amount_paid = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways_to_make_change = [1] + [0]*amount_paid

for coin in coins:
	for i in range(coin, amount_paid + 1):
		ways_to_make_change[i] += ways_to_make_change[i - coin]

print("Ways to make change for " + str(amount_paid) + " is " + str(ways_to_make_change[amount_paid]))
# answer is 73682