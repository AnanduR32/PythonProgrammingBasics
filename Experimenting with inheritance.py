class Parent:
    value1="This is value 1"
    value2="This is value 2"
class Child(Parent):
    pass
parent=Parent()
child=Child()
print(parent.value1)
print(child.value2)


