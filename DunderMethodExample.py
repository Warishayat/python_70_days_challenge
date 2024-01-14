#here i will solve the example of the dunder method or the magic method
#####   __str__ method
class student:
    def __init__(self,name,classs):
        self.name=name
        self.classs=classs

    def display(self):
        print(f"This is {self.name} and class is {self.classs}")
    def __str__(self):
        return f"Name is {self.name} and class is {self.classs}"

rafay=student("rafay","class 3")
print(rafay)



#repr

class rafay:
    def __init__(self,classs,rollnum):
        self.classs=classs
        self.rollnum =rollnum
    
    def __repr__(self):
        return f"class is {self.classs} and rollnum is {self.rollnum}"
    
a=rafay("tabish","Sp21368")
print(a)


#__len__
class university:
    def __init__(self,l):
        self.l=l
    def __len__(self):
        return len(self.l)
l=[12,13,14,15,16,17,18]
uni=university(l)
print(len(uni))

#