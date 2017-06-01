total = 0
prev = 1
num = 1

while(num < 4000000):
    fib = num + prev
    if (fib % 2 == 0):
        total += fib
    prev = num
    num = fib
    
print(total)