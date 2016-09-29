import sys

sieve = [True]*2001001
sieve[0] = False
sieve[1] = False
for i in range(2, 2001001):
    if sieve[i]:
        for j in range(2*i, 2001001, i):
            sieve[j] = False

primes = []
for i in range(0, 1001):
    if sieve[i]:
        primes.append(i)

best_a = 0
best_b = 0
best_run = 0

for a in range(-999, 1000):
    for b in primes:
        n = 0
        while sieve[n*n + a*n + b]:
            n += 1
        if n > best_run:
            best_run = n
            best_a = a
            best_b = b

print best_a, best_b, best_run, best_a * best_b