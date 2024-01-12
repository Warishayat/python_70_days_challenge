# dir __dict__ and help method in python
# x=[1,2,3,4,5,6]
# print(dir(x))
# print(x.__add__)            
# print(x.__str__)            

class person:
    def __init__(self,name,section):
        self.name=name
        self.section=section
    def displayInfo(self):
        print(f"This is {self.name} and his/her section is {self.section}")
waris=person("waris","4Aa-afternoon")
print(waris.__dict__)           #identify the attribute of the classs
# print(help(person))
