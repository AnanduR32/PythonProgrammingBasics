print("Program To Find Sum Of n even Natural Numbers\n")
num=int(input("Enter the number of even natural numbers whose sum you wish to find out\n"))
print("Value: ")
i=0
c=0
z=0
print(i,end=' ')
while(c<num):
    c=c+1
    i=i+2
    z=z+i
    if(i%2==0):
        print("+",i,end=' ')      
    
    
print("\nSum= ",z)
print("End of program")
print("Press 'Enter' key to exit")
o=input()

