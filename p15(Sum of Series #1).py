print("This program is to find the sum of series '1/1+1/2+1/3+...+1/n..")
s=0
i=1
n=int(input("Enter the value of n: "))
while(i<=n):
    s=s+(1/i)
    i=i+1
print("Sum is ",s)

