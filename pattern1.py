string1=raw_input("Enter the sentence ")
pattern=raw_input("Enter the pattern ")
i=0;j=len(pattern);counter=0;flag=0;string2=""
while(i<=(len(string1)-len(pattern))):
	string2=string1[i:j]
	if(string2==pattern):
		counter+=1
		flag=1
		print"The ",counter,"th instance is located at",i 
	i+=1
	j+=1
if(flag==1):
	print "\nPattern found at ",counter," instances"
else:
	print "\nPattern not found"		
