Till=int(input("Enter the upper limit\n"))
From=int(input("Enter the lower limit\n"))
i=1
print("\n")
while(From<=Till):
    if((From%4==0)and(From%100!=0))or(From%400==0):
        print(From)
    From+=1
input()

