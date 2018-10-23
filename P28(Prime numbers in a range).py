upper=int(input("Enter the upper bound limit\n"))
lower=int(input("Enter the lower bound limit\n"))
num=lower
print("\n")
while(num<=upper):
    check=2
    carry=0
    while(check<=(num//2)):
        if(num%check==0):
            carry=1
            break
        check+=1
    if(carry==0):
        print (num)
    num+=1
input("Press 'Enter key' to close application")
