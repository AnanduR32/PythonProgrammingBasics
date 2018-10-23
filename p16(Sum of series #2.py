print("This program is to find the sum of series '1+x^1+x^2+x^3+x^4...x^n..")
s=0
i=0
x=float(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
while(i<=n):
    s=(s+x**i)
    i=i+1
s=int(s)
print("Sum is ",s)

