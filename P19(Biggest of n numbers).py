print("Program to find the largest among n numbers")
n=int(input("Enter the number of numbers whose sum you'd like to find "))
print("Enter the value(s) ")
i=1
s=0
while(i<=n):
    a=int(input())
    if(a>s):
        s=a
    i=i+1
print("The largest number is ",s)
input()
