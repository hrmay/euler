from math import sqrt

#returns all prime factors (besides 1)
def factor(num):
	factors = list()
	for i in range(2, num//2+1):
		if num == 1:
			#fully factored
			break
		else:
			while num % i == 0:
				num = num // i
				factors.append(i)
				
	if len(factors) == 0:
		#num is prime, so it's its own prime factor
		factors.append(num)
		
	return factors
	
def isPrime(num):
	if num == 2:
		return True
	elif num % 2 == 0:
		return False
	else:
		for i in range(3,int(sqrt(num))+1,2):
			if num % i == 0:
				return False
		return True