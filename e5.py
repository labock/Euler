def isDivisible(num):
	for x in range(1,20):
		if(num%x != 0):
			#print str(num)+" is not divisible by 1-20"
			return True
	return False

index=2520
flag=True
while(flag):
	index += 1
	flag = isDivisible(index)
print str(index)+" is divisible by 1-20!"


