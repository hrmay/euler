"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from lib import factor as f

allFactors = list()

for i in range(2,21):
    iFactors = f.factor(i)
    for iFactor in iFactors:
        if iFactor in allFactors:
            allFactors.remove(iFactor)
    allFactors.extend(iFactors)

product = 1
for allFactor in allFactors:
    product = product * allFactor

print("Smallest number evenly divisible by 1-20:\n" + str(product))
