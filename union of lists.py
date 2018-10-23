list1,list2,dup=[],[],[]
Nlist1=int(input("Enter the total number of items in list 1"))
Nlist2=int(input("Enter the total number of items in list 2"))
print("Enter the elements of list 1")
for i in range(0,Nlist1):
    item=input()
    list1.append(item)
print("Enter the elements of list 2")
for i in range(0,Nlist2):
    item=input()
    list2.append(item)
for i in range(0,len(list1)):
    key=list1[i]
    for j in range(0,len(list2)):
        value=list2[j]
        if(key==value):
            dup.append(list2[j])
for i in range(0,len(dup)):
    list1.remove(dup[i])
print(list1+list2)
input()

