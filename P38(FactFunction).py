def facT(num):
    if(num==1):
        return 1
    else:
        return num*facT(num-1)
num=0;n=0
n=int(input("Enter the number whose factorial is to be found"))
print("The factorial is ",facT(n))
input()
