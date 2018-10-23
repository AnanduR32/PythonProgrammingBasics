print("To invert numbers")
a=int(input("Enter the number which you want to invert, example 123 to 321\n\n"))
b=int(a)
x=0
c=0
while(b!=0):
    c=c%10
    x=x*10+b
    b=b/10
print("The number is now: ",x)
