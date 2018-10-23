print("Program To Find Sum Of n Natural Numbers\n")
num=int(input("Enter the number of natural numbers whose sum you wish to find out\n"))
print("Value: ")
i=1
s=0
print(i,end=' ')
while(i<=num):
    s=s+i
    i=i+1
    if(i<=num):
        print("+",i,end=' ')      
    
    
print("\nSum= ",s)
print("End of program")
print("Press 'Enter' key to exit")
o=input()

