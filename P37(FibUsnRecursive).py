num=0;count=0;i=0
def fib(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return (fib(num-1)+fib(num-2))
num=0;count=0;i=0
num=int(input("Enter the nth fibonacci number till which the fabonacci numners are to be printed "))
while(i<=num):
    print(fib(i),end=' ')
    i+=1
input()
