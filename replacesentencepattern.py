sentence=input("Enter the sentence")
pattern=input("Enter the pattern")
replace=input("Enter the new pattern")
position=[];extracts=[]
count=0
j=len(pattern)
for i in range(0,len(sentence)):
    for j in range(i+1,len(sentence)):
        extract=sentence[i:j]
        if(extract==pattern):
            extracts.append(extract)
            position.append(i)
            count+=1
for i in extracts:
    sentence=sentence.replace(i,replace)
if(count>0):
    print("The pattern was located at following locations",position,"\nNumber of instance of the pattern found=",count)
else:
    print("No instances of pattern was found to be removed")
print(sentence)
    
