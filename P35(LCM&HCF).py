print("Press 1 to find LCM of two numbers\n")
print("Press 2 to find HCL of two numbers\n")
choice=int(input("Enter choice (1-2)\n\n"))
num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second numbers\n"))
i=1
factor=1
if(num1>num2):
    sml=num2
    grt=num1
else:
    sml=num1
    grt=num2
if(choice==1):
    while(True):
        if((grt%num1==0)and(grt%num2==0)):
            factor=grt
            break
        grt+=1
elif(choice==2):
    while(i<=sml):
        if((num1%i==0)and(num2%i==0)):          
                factor=i
        i+=1
else:
    print("\nInvalid Entry")
print("\nThe output is ",factor)
input()
