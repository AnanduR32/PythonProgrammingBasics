lower=int(input("Enter the value for the lower bound limit: "))
upper=int(input("Enter the value for the upper bound limit: "))
numLoop=lower
c=0
while(numLoop<=upper):
    num=numLoop
    numcount=numLoop
    Sum=0
    Digit=0
    count=0
    while(numcount!=0):
        numcount=numcount//10
        count+=1
    while(num!=0):
        Digit=num%10
        Sum+=(Digit**count)
        num=num//10
    if(Sum==numLoop):
        print(numLoop)
        c+=1
    numLoop+=1
if(c==0):
    print("\n\nThere are not armstrong numbers within this range")
input("\nPress 'Enter key' to exit")
