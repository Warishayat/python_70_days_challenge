#static method
class math:
    def __init__(self,num):
        self.num=num
    def multiplaywithN(self,n):
        self.num=self.num*n
        print("The multiplivation of n is:",self.num)

    @staticmethod    
    def exponent(n,m): #no need to pass self arguments in static method...
        return n**2+m**2
# static method dont have any link with class instance even class they can execute without
# instance and class name or with the class name.<===>
py=math(12)       
py.multiplaywithN(4)
# print(py.exponent(2,3))             #call with instane name
print(math.exponent(4,3))           #call with class name
