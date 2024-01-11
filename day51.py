#in today class i will cover the alternate constructor
class student:
    def __init__(self,name,dept,rollnum):
        self.name=name
        self.dept=dept
        self.rollnum=rollnum
    @classmethod
    def strMethod(cls,str):
        return cls(str.split(",")[0],str.split(",")[1],str.split(",")[2])
str="Waris,Software_Enginnering,Sp21368"
a=student.strMethod(str)
print(a.name)
print(a.rollnum)
print(a.dept)