a=int(input("enter the limit"))
for i in range(0,a+1):
    for j in range(0,i):
        if ((i+j)%2==0):
            print ("0",end='')
        else:
            print ("1",end='')
    print ('')
input()
