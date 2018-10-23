sentence=input("Enter the sentence")
pattern=input("Enter the pattern")
position=[]
count=0
j=len(pattern)
for i in range(0,len(sentence)):
    for j in range(i+1,len(sentence)):
        extract=sentence[i:j]
        if(extract==pattern):
            position.append(i)
            count+=1
if(count>0):
    print("The pattern was located at following locations",position,"\nNumber of instance of the pattern found=",count)
else:
    print("No instances of pattern was found")
    
