n=int(input("Enter the number\n"))
carry=0
for i in range(2,n//2):
    if(n%i==0):
        carry=1
        break
    i+=1
if(carry==0):
    print("The number is a prime number")
else:
    print("The number is not a prime number")
input("\nPress 'Enter key' to exit")
