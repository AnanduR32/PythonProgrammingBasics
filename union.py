list1=[]
list2=[]
extracts=[]
num1=int(input("Enter the items of list 1"))
num2=int(input("Enter the items of list 2"))
print("\nEnter the items of list 1")
for i in range(0,num1):
    item=input()
    list1.append(item)
for i in range(0,num2):
    item=input()
    list2.append(item)
for i in range(0,num1):
    for j in range(i+1,num1):
        if(list1[i]==list2[j]):
            extract=list1[j]
            extracts.append(extract)
for i in extracts:
    list1.remove(i)
for i in list1:
    list2.remove(i)
print(list1)
