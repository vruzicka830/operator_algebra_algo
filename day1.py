def multiply_by_two(x):
	return x * 2

def compute_factorial(n):
	if type(n) is not int:
		raise TypeError("The input must be a nonnegative integer.")
	if n < 0:
		raise TypeError("The input must be a nonnegative integer.") # This should be a ValueError, since it's technically 
# the right type.
	result = 1
	if n == 0: # Actually don't need this, because range(0) is an empty sequence so that the
# for loop just exists immediately (without looping). Thus the function would just return result = 1.
		return result
	for i in range(n):
		result = result * (i+1) # Just use result *= (i+1)
	return result
# Note that this is 8 space indent, while "industry standard" is 4 space

def is_prime(n):
	if type(n) is not int:
		raise TypeError("a prime is an integer")
	if n < 2:
		raise ValueError("a prime is a positive integer "
"that's at least 2")
	result = "not sure"
	if n==2 or n==3 or n==5:
		return "prime"
	numbers = range(6,n,6)
	if n%2 == 0:
		return "not prime, it's even"
	if n%3 == 0:
		return "not prime, divisible by three"
	if n%5 == 0:
		return "not prime, divisible by five"
	for i in range(0,int(n**0.5)):
		if n%(numbers[i]+1) ==0 and n!=(numbers[i]+1):
			return "not prime"
		if n%(numbers[i]+5) ==0 and n!=(numbers[i]+5):
			return "not prime"
		if n == numbers[i]+1 or n==numbers[i]+5:
			return "prime"

def is_prime_new(n):

	if type(n) is not int:
		raise TypeError("a prime is an integer")
	if n < 2:
		raise ValueError("a prime is a positive integer that's at least 2")

	initial_primes=[2,3,5,7,11,13,17,19,23]

	for i in initial_primes:
		if n==i:
			return True
		if n%i==0:
			return False

	new_primes=[]
	i=1
	while 6*i-1<= int(n**0.5):
		if 6*i+1 > max(initial_primes):
			new_primes.append(6*i-1)
			new_primes.append(6*i+1)
		if n%(6*i-1)==0 or n%(6*i+1)==0:
			return False
		i=i+1

	if not new_primes:
		return True

	return True
