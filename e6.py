sumOfSquares=0
sum=0
for x in range(1,101):
	square=x*x
	sumOfSquares+=square
	sum+=x
squareOfSum=sum*sum
diff=squareOfSum-sumOfSquares
print "Sum           : "+str(sum)
print "Square of Sum : "+str(squareOfSum)
print "Sum of Squares: "+str(sumOfSquares)
print diff
