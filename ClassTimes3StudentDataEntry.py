import pickle 
class StudenT:
    def initialize(student):
        print("""---------------STUDENT'S DATABASE--------------------

        Enter your choice:
        
        1.Input Data of Students
        2.Edit details of a Student
        3.Display data of a Student
        """)
        student.choice=int(input("\vEnter your choice: "))
    def getdata(student):
        student.name=str(input        ("Enter the name of student                            :"))
        student.age=int(input         ("Enter the age of student                             :"))
        student.regno=str(input       ("Enter the registration number of student             :"))
        student.markA=float(input     ("Enter the marks scored by for Series 1 internal exam :"))
        student.markB=float(input     ("Enter the marks scored by for series 2 internal exam :"))
        student.assgnmentA=float(input("Enter the marks scored for first assignment          :"))
        student.assgnmentB=float(input("Enter the marks scored for second assignment         :"))
        student.assgnmentC=float(input("Enter the marks scored for third assignment          :"))
        student.morale=str(input      ("Enter morale level of the student on scale of (0-10) :"))
    def calc(student):
        student.mark=student.markA+student.markB
        student.assgnment=(student.assgnmentA+student.assgnmentB+student.assgnmentC)/3
        student.Mark=student.mark+student.assgnment
    def display(student):
        print("------------------STUDENT DETAILS-----------------------")
        data={}
        f=open("R:\StudentDetailsSessional2.txt","rb")
        data=pickle.load(f)
        if(student.choice==3):
            Roll=int(input("Enter roll number of student whose details you'd like to have displayed: "))
            print("\n\tDisplaying details of Student")
            print("--------------------------------------------------------------------------")    
            print("\t\tStudent's name                :",data[Roll][0])
            print("\t\tStudent's age                 :",data[Roll][1])
            print("\t\tStudent's registration number :",data[Roll][2])
            print("\t\tStudent's Final Sessional mark:",data[Roll][3])
            print("--------------------------------------------------------------------------")
        else:
            for i in len(data):                
                print("\n\tDisplaying details of Student")
                print("--------------------------------------------------------------------------")    
                print("\t\tStudent's name                :",data[i][0])
                print("\t\tStudent's age                 :",data[i][1])
                print("\t\tStudent's registration number :",data[i][2])
                print("\t\tStudent's Final Sessional mark:",data[i][3])
        f.close()
    def changeD(student):
        f=open("R:\StudentDetailsSessional2.txt","rb")
        data=pickle.load(f)
        data[Student.keyV][0]=str(input("Enter new name                :"))
        data[Student.keyV][1]=int(input("Enter new age                 :"))
        data[Student.keyV][2]=str(input("Enter new registration number :"))
        data[Student.keyV][3]=int(input("Enter new Sessional Score     :"))
        f.close
        f=open("R:\StudentDetailsSessional2.txt","wb")
        pickle.dump(data,f)
        f.close
    def Initialize(student):
        rollN=int(input("Enter the total number of students in class   :"))
        student.roll={};listA=[]
        for key in range(1,rollN+1):
            student.key=key
            print("Enter details of student who has been assigned the roll number:",key)
            Student.getdata()
            Student.calc()
            listA=[student.name,student.age,student.regno,student.Mark]
            student.roll[key]=listA
    def Save(student):
        f=open("R:\StudentDetailsSessional2.txt","wb")
        pickle.dump(student.roll,f)
        f.close()
Student=StudenT()
while(True):
    Student.initialize()
    if(Student.choice==1):
        Student.Initialize()
        Student.Save()
    elif(Student.choice==2):
        print("Enter the roll number of student whose data you'd like to edit  :")
        Student.keyV=int(input())
        Student.changeD()
    elif(Student.choice==3):
        Student.display()
    print("""\nWould you like to continue?
press 'Y' to continue, 'N' to close""")
    exiT=input()
    exiT.lower()
    if(exiT=='y'):
        continue
    elif(exiT=='n'):
        break
            
                   
        
        
    
        
        


        
        
        
