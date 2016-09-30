# Python 3

pyramid = [map(int, s.split()) for s in open('problem-67-pyramid.txt').readlines()]

# Start at last row - i.e. the bottom - and move to the top
for row in range(len(pyramid)-1, 0, -1): 
    for col in range(row):
        pyramid[row-1][col] += max(pyramid[row][col], pyramid[row][col+1])

print( "Maximum = " +  str(pyramid[0][0]) )