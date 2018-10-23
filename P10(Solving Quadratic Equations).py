print("FINDING ROOTS OF A QUADRATIC EQUATION\n\n")
print("Any general quadratic equation will be of the form 'ax^2+bx+c=0', \ntherefore state values...")
a=int(input("\tcoefficient of x^2, a= "))
b=int(input("\tcoefficient of x, b= "))
c=int(input("\tconstant, c= "))
x=(b**2)-4*a*c
if(x==0):
    print("\nThe roots are equal\nThe roots are")
    r1=(-b/2*a)
    r2=(-b/2*a)
    print("\t",r1)
    print("\t",r2)
elif(x>0):
    print("The roots are real and unequal\nThe roots are")
    r1=(-b+(x**(1/2)))/2*a
    r2=(-b-(x**(1/2)))/2*a
    print("\t",r1)
    print("\t",r2)
else:
    print("The roots are imaginary and unequal\nThe roots are")
    r1=(-b/2*a)
    r2=((-x)**(1/2))/2*a
    print("\t",r1,"+i",r2)
    print("\t",r1,"-i",r2)
print("\n\nProgram Ends, Press 'Enter' key to close")
i=input()








    
    
