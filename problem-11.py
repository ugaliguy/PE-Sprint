# Python 3

# Largest product in a grid

g = [map(int, s.split()) for s in open('problem-11-grid.txt').readlines()]

maxprod = 0
grid_trans = [list(i) for i in zip(*grid)] # Transpose of grid
adjacent = 4
for row in range(len(grid)):
	for col in range(len(grid_trans)-adjacent + 1):
		maxrow = max(grid[row][col]*grid[row][col+1]*grid[row][col+2]*grid[row][col+3], grid_trans[row][col]*grid_trans[row][col+1]*grid_trans[row][col+2]*grid_trans[row][col+3])
		if row < len(grid) - adjacent:
			maxdiag = max(grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3], grid[row][col+3]*grid[row+1][col+2]*grid[row+2][col+1]*grid[row+3][col])
		maxprod = max(maxprod,maxrow,maxdiag)
		
print(maxprod) # 70600674