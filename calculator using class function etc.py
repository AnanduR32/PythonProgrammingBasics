class Calculator:
    def readValue(key):
        choice=input("""Enter your choice
Whether you wish to perform addition, subtraction,
division or multiplication?..

     The Choice is yours : """)
        valueA=input("\nEnter value A: ")
        valueB=input("Enter value B: ")
        key.valueA=valueA
        key.valueB=valueB
        key.choice=choice
    def performFunc(key):        
        if(key.choice=='add')or(key.choice=='+')or(key.choice=='sum')or(key.choice=='plus'):
            result=key.addition(int(key.valueA),int(key.valueB))
        if(key.choice=='sub')or(key.choice=='-')or(key.choice=='minus'):
            result=key.subtraction(int(key.valueA),int(key.valueB))
        if(key.choice=='mul')or(key.choice=='*')or(key.choice=='product')or(key.choice=='x'):
            result=key.multiplication(int(key.valueA),int(key.valueB))
        if(key.choice=='div')or(key.choice=='/'):
            result=key.division(int(key.valueA),int(key.valueB))
        key.result=result
    def addition(key,a,b):
        return a+b
    def multiplication(key,a,b):
        return a*b
    def subtraction(key,a,b):
        return a-b
    def division(key,a,b):
        return a/b
    def output(key):
        print("Output of function is ",key.result)
calc=Calculator()
calc.readValue()
calc.performFunc()
calc.output()

    
        
