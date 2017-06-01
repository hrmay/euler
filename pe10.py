"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from lib import factor as f

#Account for the only even prime
total = 2

for i in range(3, 2000000, 2):
    if f.isPrime(i):
        total += i

print("Sum of primes under two million:\n" + str(total))
