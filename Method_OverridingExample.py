# Let's consider a scenario involving multiple levels of inheritance. You'll create a base
# class Person, a derived class Employee that inherits from Person, and another derived class 
# Manager that inherits from Employee. Your task is to override a method in each class to 
# add specific behavio

class person:
    def __init__(self,name):
        self.name=name
    def displayinfo(self):
        print(f"The name is {self.name}")
class employe(person):
    def __init__(self,name,id):
        super().__init__(name)
        self.name=name
        self.id=id
    def displayinfo(self):
        print(f"The name is {self.name} and employe if {self.id}")
class manager(employe):
    def __init__(self,name,id,post):
        super().__init__(name,id)
        
        self.post=post
    def displayinfo(self):
        print(f"The name is {self.name} against id {self.id} and post is {self.post}")

waris=manager("waris","Sp21368","Ceo")
waris.displayinfo()