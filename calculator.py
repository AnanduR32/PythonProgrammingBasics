def add(a,b):
	return float(a+b)
def sub(a,b):
	return float(a-b)
def mul(a,b):
	return float(a*b)
def div(a,b):
	return float(a/b)
a=0;b=0;
print("""Enter you choice(1-4)
		
	   1.Addition of two numbers
	   2.Subtration of second number from first
	   3.Multiplication of two numbers
	   4.Divion of first number from the second
	
	Enter your choice""")
choice=int(input())
if(choice<=4)and(choice>=1):
	a=float(input("Enter the first number"))
	b=float(input("Enter the second number"))
	if(choice==1):
		print("The sum is ",add(a,b))
	elif(choice==2):
		print("The subtraction result is ",sub(a,b))
	elif(choice==3):
		print("The multiplication result is ",mul(a,b))
	elif(choice==4):
		print("The division result is ",div(a,b))
else:
	print("Invalid Entry")

