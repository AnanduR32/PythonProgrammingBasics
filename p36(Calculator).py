num1=0;num2=0;ip1=0;ip2=0;choice=0;
def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return num1*num2   
def div(num1,num2):
    return num1/num2    
def sub(num1,num2):
    return num1-num2   
print("""Select you choice(1-4):

         1.Addition of two numbers
         2.Subtraction of second number from first
         3.multiplication of two numbers
         4.Division of first number by second
         \n""")
choice=int(input("Enter your choice"))
if(choice>4)or(choice<1):
    print("Invalid Choice")
else:
    ip1=float(input("Enter the first number"))
    ip2=float(input("Enter the second number"))
    if(choice==1):
        print(add(ip1,ip2))
    elif(choice==2):
        print(sub(ip1,ip2))
    elif(choice==3):
        print(mul(ip1,ip2))
    elif(choice==4):
        print(div(ip1,ip2))
input()
