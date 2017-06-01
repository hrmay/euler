"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from lib import factor as f

i = 1
test = 2
prime = 2

while i <= 10001:
    factors = f.factor(test)
    if len(factors) == 1:
        i += 1
        prime = test
        
    if test == 2:
        test += 1
    else:
        test += 2

print("10,001st prime:\n" + str(prime))
