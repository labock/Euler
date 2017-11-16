import math

def isTriplet(a,b,c):
	if(a*a + b*b == c*c):
		return True
	return False

def sums1k(a,b,c):
	if(a+b+c == 1000):
		return True
	return False	

for a in range(1,500):
	for b in range(1, 500):
		for c in range(1, 500):
			if(isTriplet(a,b,c) and sums1k(a,b,c)):
				print a
				print b
				print c
			c+=1
		b+=1
	a+=1




