print("Printing n fibonacci numbers")
i=1
x=0
y=1
p=int(input("How many numbers would you like to have displayed: "))
while(i<=p):
    print(x,end=' ')
    s=x+y
    x=y
    y=s
    i=i+1
print("\n\nEnd of Program\n")
print("Press \"Enter key\" to exit")
u=input()
