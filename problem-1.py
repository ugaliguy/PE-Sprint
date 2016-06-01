# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

upper_bound = 999
div_3 = upper_bound//3
div_5 = upper_bound//5
div_15 = upper_bound//15

sum_3 = 3*div_3*(div_3 + 1)/2
sum_5 = 5*div_5*(div_5 + 1)/2
sum_15 = 15*div_15*(div_15 + 1)/2

answer = sum_3 + sum_5 - sum_15

print(answer)