def frcount(num):
        if(num==1):
                print('1')
                return 1
        else:
                print (num)
                return (frcount(num-1))
print()
num=input("Enter the number")
frcount(num)
