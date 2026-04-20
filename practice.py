###########################################################
def multiply_by_two(x): # Multiply a number by two.
	return x * 2

def compute_factorial(n): # Compute the factorial of a nonnegative integer.
    # Check that input is an integer
    if type(n) is not int:
        raise TypeError("The input must be a nonnegative integer.")

    # Check that input is nonnegative
    if n < 0:
        raise ValueError("The input must be a nonnegative integer.")

    result = 1
    for i in range(n):
        result *= (i + 1)

    return result

def is_prime(n): # Determine if a number is prime.
    if type(n) is not int:
        raise TypeError("Input must be an integer.")

    if n < 2:
        raise ValueError("Input must be at least 2 to check for primality.")

    # Handle small primes directly
    if n == 2 or n == 3 or n == 5 or n==7 or n==11 or n==13 or n==17 or n==19 or n==23:
        return True
    if n % 2 == 0 or n % 3 == 0 or n%5==0 or n%7==0 or n%11==0 or n%13==0 or n%17==0 or n%19==0 or n%23==0:
        return False

    # If you get to here, n \geq 29.
    i = 1
    while (6 * i - 1) <= int(n**0.5):
        # Check both 6k-1 and 6k+1
        if n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0:
            return False
        i += 1

    # If no divisors were found, n is prime
    return True
