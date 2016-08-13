problem-9.py

# Python 3

# 	Special Pythagorean triplet
# Find Pythagorean triplet (a,b,c) such that a + b + c = 1000

answer = 0
for c in range(500,2,-1):
    if answer != 0:
        break
    for b in range(c-1,2,-1):
        a = 1000 - (c + b)
        if c**2 == (a**2 + b**2):
            answer = a*b*c
            print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
            break

print("The answer is " + str(answer))