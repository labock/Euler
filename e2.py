termA=1
termB=2
sum=2
it=1

while(termB<4000000):
	print "Iteration "+str(it)+": Term A = "+str(termA)+" Term B = "+str(termB)+ " Sum = "+str(sum)
	nextTerm = termA + termB
	termA = termB
	termB = nextTerm
	it+=1
	if(nextTerm%2==0):
		sum+=nextTerm