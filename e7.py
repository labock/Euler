def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def nthPrime(n):
	candidate=2
	count=0
	while(count<n):
		if(isprime(candidate)):
			count+=1
		candidate+=1
	return candidate-1

print nthPrime(10001)
