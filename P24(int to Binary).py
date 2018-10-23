i=1
s=0
dec=int(input("Enter the number\n"))
while(dec>0):
    rem=int(dec%2)
    s=s+(i*rem)
    dec=int(dec/2)
    i=i*10
print(s)
input("Press 'Enter' Key to exit")
