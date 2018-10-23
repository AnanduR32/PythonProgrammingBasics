
sentence=raw_input("Enter the sentence")
pattern=raw_input("Enter the pattern in the above sentence that is to be replaced")
npattern=raw_input("Enter the pattern which replaces the above pattern")
string="";i=0;j=len(pattern)
new=""
while(i<=(len(sentence)-len(pattern))):
	string=sentence[i:j]
	if(string==pattern):
		sentence=sentence.replace(string,npattern)
	
	i+=1
	j+=1
print sentence







