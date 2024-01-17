#single inheritance

class student:                          #parent class
    def __init__(self):
        self.name="waris"
        self.rollnum="Sp-21368"
    def __repr__(self):
        return f"Name is {self.name} & rollnum is {self.rollnum}"
    
class university(student):                  #child class
    def __init__(self,section,depart):
        super().__init__()
        self.section=section
        self.depart=depart
    def __str__(self):
        return f"Name is {self.name} Against Rollnum {self.rollnum} where section is {self.section} and department is{self.depart}"
    

waris=university("4A-Afternoon","Software-Engineering")
print(waris)



#multiple inheritance

class uni:
    def __init__(self,name):
        self.name=name
        
    def display(self):          #Method 
        print(f"The name of the institute is {self.name}")

class stud:
    def __init__(self,stud):
        self.stud=stud
    def display(self):          #dipslay Method 
        print(f"The name of the stud is {self.stud}")

class department(stud,uni):
    def __init__(self,name,stud):
        self.name=name
        self.stud=stud
    def display(self):             #Display Method override
        print(f"The name is {self.name} and student is {self.stud}")
print(department.__mro__)
waris=department("NUML University","Waris-Hayat")
waris.display()



# #Multi-Level Inheritance

class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"The name is {self.name}")
class cast(student):
    def __init__(self,name,cast):
        super().__init__(name)
        self.cast=cast
    def display(self):
        print(f"The cast against name{self.name} is {self.cast}")
class car(cast):
    def __init__(self,name,cast,color,model):
        super().__init__(name,cast)
        self.color=color
        self.model=model
    def display(self):
        print(f"The car name is {self.model} and color is {self.color} Owner is {self.name} and cast is {self.cast}")
waris=car("Waris-Hayat","Abbasi","Balack","Honda")
waris.display()
