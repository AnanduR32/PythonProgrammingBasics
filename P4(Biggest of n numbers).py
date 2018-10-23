print("FINDING WHICH IS THE BIGGEST NUMBER")
print("To find  biggest of two numbers press 1 ")
print("To find biggest of three numbers press 2")
z=int(input("Enter choice(1-2)"))
if(z==1):
        a=float(input("Enter the first number\n"))
        b=float(input("Enter the second number\n"))
        if(a>b):
                print("The biggest number is\n",a)
        else:
                print("The biggest number is\n",b)
        print("bubye")
elif(z==2):
        a=float(input("Enter the first number\n"))
        b=float(input("Enter the second number\n"))
        c=float(input("Enter the third number\n"))
        if(a>b):
                if(a>c):
                        print("The biggest number is\n",a)
                else:
                        print("The biggest number is\n",c)
        else:
                if(b>c):
                        print("The biggest number is\n",b)
                else:
                        print("The biggest number is\n",c)
        print("bubye")
else:
        print("Invalid entry... you should cease your existance.....\n")
x=input("Enter button..please...i begs\n")

