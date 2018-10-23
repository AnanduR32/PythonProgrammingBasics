def fib(n,d):
    if(n in d):
        result=d[n]
    elif(n==1)or(n==2):
        result=1
    elif(n==0):
        result=0
    else:
        result=fib(n-1,d)+fib(n-2,d)
        d[n]=result
    return result
term=0
listA=[]
n=0
num=int(input("Enter value n, the nth fibonacci number "))
d={}
for i in range(0,num):
    term=fib(i,d)
    listA.append(term)
print("The ",num,"th term is ",term)
print("The Fibonacci series till ",n," is :\n",listA)
input()
    
