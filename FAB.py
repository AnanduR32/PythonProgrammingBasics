def fib(iteration):
	if(iteration==1):
		return 1
	elif(iteration==0):
		return 0
	else:
		return fib(iteration-2)+fib(iteration-1)
iteration=0;num=0
print"Enter the n'th number till which\nthe fibonacci numbers are to be printed"
num=int(input())
print
while(iteration<=num):
	print fib(iteration),
	iteration=iteration+1
