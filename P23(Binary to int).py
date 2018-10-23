i=1
s=0
dec=int(input("Enter the value of number\n"))
while(dec>0):
    rem=int(dec%10)
    s=s+(i*rem)
    dec=int(dec/10)
    i=i*2
print("\n")
print(s)
input()
