import math
def mul(a,b):
	return a*b
def circle(a):
	return math.pi*a**2
print("""\nEnter your choice(1-4):
	  
	   1.Finding the area of a square
	   2.Finding the area of a rectangle
	   3.Finding the area of a triangle
	   4.Finding the area of a circle""")
choice=int(input())
if(choice>=1)and(choice<=3):
	a=float(input("Enter the length/height "))
	b=float(input("Enter the breadth "))
	print("\nThe area is ",end='')
	if(choice==1)or(choice==2):
		print (mul(a,b))
	elif(choice==3):
		print (mul(a,b)/2)
elif(choice==4):  
	a=float(input("Enter the radius of the circle "))
	print("\nThe area is ",end='')
	print (circle(a))
else:
	print("Invalid choice")

	
