"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        productStr = str(product)
        front = productStr[:(len(productStr)//2)]
        if (len(productStr) % 2 == 0):
            back = productStr[len(productStr):(len(productStr)//2)-1:-1]
        else:
            back = productStr[len(productStr):(len(productStr)//2):-1]

        if (front == back) and (product > largest):
            largest = product
            num1 = i
            num2 = j

print("Largest palindrom product of two 3-digit numbers:\n" + str(largest))
