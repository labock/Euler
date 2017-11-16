def isPalindrome(x):
	return str(x) == str(x)[::-1]

max=0
for x in range(100, 1000):
	for y in range(100, 1000):
		product=x*y
		if(isPalindrome(product) and product>max):
			max=product
print max