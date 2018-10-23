def ftensum(num):
	if(num==1):
		return 1
	else:
		return num+ftensum(num-1)
num=0
print
print"The sum of the first 10 natural numbers is ",ftensum(10)
print
