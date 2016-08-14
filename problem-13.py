# Python 3

# Large Sum


# Learn how to deal with input/output
large = [map(int, s.split()) for s in open('problem-13-grid.txt').readlines()]

#large = [int(i) for i in large.split("\n")]

big_sum = sum(large)
print(big_sum) # 5537376230390876637302048746832985971773659831892672