print("Program to find the sum of series 1+(1+2)+(1+2+3)+(1+2+...n")
s=0
i=1
j=0
n=int(input("Enter the value of n "))
while(i<=n):
    c=1
    j=0
    while(c<=i):
        j=j+c
        c=c+1
    s=s+j
    i=i+1
print("The sum of values is ",s)
input()
