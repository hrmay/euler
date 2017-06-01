"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from lib import factor as f

factors = f.factor(600851475143)

print("Largest prime factor of 600851475143 is\n" + str(max(factors)))
