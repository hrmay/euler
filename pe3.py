"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def factor(num):
    factors = set()
    for i in range(2, num//2):
        if num == 1:
            #fully factored
            break
        else:
            while num % i == 0:
                num = num // i
                factors.add(i)
                print(i)
    return factors

factors = factor(600851475143)

print("Largest prime factor of 600851475143 is\n" + str(max(factors)))
