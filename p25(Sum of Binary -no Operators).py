da=int(input("Enter the number\n"))
db=int(input("Enter the number\n"))
i=1
s1=0
ra=0
s2=0
rb=0
while(da>0):
    ra=int(da%10)
    s1=s1+(i*ra)
    da=int(da/10)
    i=i*2
s1=int(s1)
i=1
s2=0
rb=0
while(db>0):
    rb=int(db%10)
    s2=s2+(i*rb)
    db=int(db/10)
    i=i*2
s2=int(s2)
s3=s1+s2
i=1
s=0
while(s3>0):
    r=int(s3%2)
    s=s+(i*r)
    s3=int(s3/2)
    i=i*10
print(s)
input("Press 'Enter' Key to exit")


    
