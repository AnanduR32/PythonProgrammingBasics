l=int(input("Enter lower limit\n"))
u=int(input("Enter upper limit\n"))
x=l
y=2
z=0
while(x<=u):
    y=2
    z=0
    while(y<=(x/2)):
        if(x%y==0):
            z=1
            break;
        y=y+1
    if(z==0):
        print(x)
    x=x+1
w=input("Press 'Enter' key to close the program")
