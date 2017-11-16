import math

def primeFactors(n):
	twoCount=0
	while(n%2 == 0):
		twoCount+=1
		n = n/2
	print "2 "*twoCount

	for i in range(3, int(math.sqrt(n))+1, 2):
		while n%i==0:
			print i,
			n=n/i

	if n>2:
		print n

primeFactors(600851475143)