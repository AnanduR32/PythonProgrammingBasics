print("Program To Find Sum Of n Natural Numbers\n")
num=int(input("Enter the number of natural numbers whose sum you wish to find out\n"))
print("Value: ")
i=0
s=0
print(i,end=' ')
while(i<=num):
    s=s+i
    i=i+2
    if(i%2==0):
        print("+",i,end=' ')      
    
    
print("\nSum= ",s)
print("End of program")
print("Press 'Enter' key to exit")
o=input()

