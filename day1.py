import math

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
		return "not prime"
	numbers = list(range(1,n+1))
	if n%2 == 0:
		return "not prime, it's even"
	if n%3 == 0:
		return "not prime, divisible by three"
	if n%5 == 0:
		return "not prime, divisible by five"
	for i in range(n):
		while 6*numbers[i]+1<math.sqrt(n):
			if n%(6*numbers[i]+1)==0 or n%(6*numbers[i]+5)==0:
				return "not prime"
	return "prime"
