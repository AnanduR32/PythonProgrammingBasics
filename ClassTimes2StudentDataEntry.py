import pickle 
class StudenT:
    def getdata(student):
        student.name=str(input("Enter the name of student"))
        student.age=int(input("Enter the age of student"))
        student.regno=str(input("Enter the registration number of student"))
        student.markA=float(input("Enter the marks scored by him/her for Series 1 internal exam"))
        student.markB=float(input("Enter the marks scored by him/her for series 2 internal exam"))
        student.assgnmentA=float(input("Enter the marks scored for first assignment"))
        student.assgnmentB=float(input("Enter the marks scored for second assignment"))
        student.assgnmentC=float(input("Enter the marks scored for third assignment"))
        student.morale=str(input("Enter morale level of the student on scale of (0-10)"))
    def calc(student):
        student.mark=student.markA+student.markB
        student.assgnment=(student.assgnmentA+student.assgnmentB+student.assgnmentC)/3
        student.Mark=student.mark+student.assgnment
    def display(student):
        print("\n\tDisplaying details of Student")
        print("--------------------------------------------------------------------------")    
        print("\t\tStudent's name                :",student.name)
        print("\t\tStudent's age                 :",student.age)
        print("\t\tStudent's registration number :",student.regno)
        print("\t\tStudent's Final Sessional mark:",student.Mark)
        print("--------------------------------------------------------------------------")    
        
Student=StudenT()
class Class:
    def getdata(RollNo):
        rollN=int(input("Enter the total number of students in class"))
        RollNo.roll={};listA=[]
        for key in range(1,rollN+1):
            RollNo.key=key
            print("Enter details of student who has been assigned the roll number: ",key)
            Student.getdata()
            Student.calc()
            listA=[Student.name,Student.Mark]
            RollNo.roll[key]=listA
    def Save(RollNo):
        f=open("R:\StudentDetailsSessional.xlsx","wb")
        pickle.dump(RollNo.roll,f)
        f.close()
classA=Class()
classA.getdata()
classA.Save()
Student.display()
            
        
        
    
        
        


        
        
        
