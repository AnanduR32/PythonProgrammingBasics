def factorial(num):
	if(num==1):
		return 1
	else:
		return num*factorial(num-1)
num=0
print"Enter the number whose factorial is to be found"	
num=float(input())
print"The factorial is ",factorial(num)

	
