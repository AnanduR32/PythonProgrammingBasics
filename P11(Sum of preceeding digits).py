a=1
b=0
c=0
print("Enter limiter\n")
n=int(input())
i=1
s=0
while(i<=n):
    while(a<10):
        print (a,"\n")
        s=s+a
        a=s
        i=i+1
    b=a
    while(i<=n):
        while(b!=0):
            c=b%10
            s=s+c
            b=b/10
            print(s,"\n")
        i=i+1
    i=i+1
print(s)
print("Enter\n")
g=input()
        
        
   
        
    
    
    
