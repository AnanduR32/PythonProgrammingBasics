print("Program to find the sum of series 1+1/2!+1/3!+1/4!...+1/n!\n\n")
s=0
i=1
j=1
n=int(input("Enter the value of n "))
while(i<=n):
    c=1
    while(c<=i):
        j=j*c
        c=c+1
    s=s+(1/j)
    i=i+1
print("The sum of values is ",s)
input()

    
