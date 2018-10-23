print("CONVERSTION BETWEEN DIFFERENT UNITS OF TEMPERATURE")

print("To change from degrees celsius to farhenheit press 1")
print("To change from degress farhenheit to celsius press 2")

a=int(input("Enter your choice, "))
 
if(a==1):
	print("Enter the temperature")
	b=float(input())
	c=b*1.8+32
	print("The temperature in farhenheit is ",c)
elif(a==2):
	print("Enter the temperature")
	d=float(input())
	e=(d-32)/1.8
	print("The temperature in celsius is ",e)
else:
	print("invalid entry")
o=input("ENTERRRRRR!!!....")

