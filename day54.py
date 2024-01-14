# dunder Method

class student:
    def __init__(self):
        self.name="waris"
        self.rollnum=21368
    
    def __repr__(self):
        return (f"Name {self.name} and rollnum is {self.rollnum}")
    
    
a=student()
print(a)


class legth:
    def __init__(self,lest):
        self.lest=lest
    def __len__(self):
        return len(self.lest)

lest=[1,2,3,4,5,6]
obj=legth(lest)
print(len(obj))



        