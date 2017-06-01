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
