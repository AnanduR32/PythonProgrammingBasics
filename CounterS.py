question=0
space=0
words=1
sentences=0
sentence=raw_input("Enter the sentence")
for i in sentence:
	if(i=='?'):
		question=question+1
	if(i==' '):
		space=space+1
	if(i==' '):
		words=words+1
	if(i=='.')or(i=='?'):
		sentences=sentences+1
print"\nThe number of questions is ",question
print"\nThe number of spaces is ",space
print"\nThe number of words is ",words
print"\The number of sentences is",sentences
