def fsum(num):
	if(num==1):
		return 1
	else:
		return num+fsum(num-1)
print"Enter the n'th number till which the sum is to be found"
num=int(input())
print"\nThe sum is ",fsum(num)
