#in day56 i will solve the overloading operator we can chage the behaviour of the operator

class student:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,other):
        return student(self.i + other.i, + self.j + other.j, + self.k + other.k)
s1=student(1,3,5)
print(s1)
s2=student(2,4,6)
print(s2)
print(s1+s2)
print(type(s1+s2))


#Another example

class university:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum

    def __str__(self):
        return f"The name is {self.name} and rollnum is {self.rollnum}"
    def __add__(self,other):
        return f"Name After concatination is {self.name + other.name} and Rollnum after {other.rollnum + self.rollnum}"
waris=university("waris","21368")
print("Dunder Method:",waris)
waris2=university("Hayat","Sp")
print(waris2)
#what if i concat the obj waris and waris2 
print(waris+waris2)

#practise
# Create a class called ComplexNumber that represents a complex number. Implement the necessary
#  methods to enable addition, subtraction, multiplication, and equality 
#  comparisons (== and !=) of two complex numbers.

class ComplexNumber:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def __add__(self,other):
        return f"{self.num1 + other.num1} {self.num2 + other.num2}"
    def __sub__(self,other):
        return f"{self.num1 - other.num1} {self.num2 - other.num2}"
    def __truediv__(self,other):
        return f"{self.num1 / other.num1} {self.num2 / other.num2}"
    def __mult__(self,other):
        return f"{self.num1 * other.num1} {self.num2 * other.num2}"
    def __eq__(self,other) :
        return f"{self.num1 == other.num1} {self.num2 == other.num2}"
    def __notEqual__(self,other):
        return f"{self.num1 != other.num1} {self.num2 != other.num2}"
obj1=ComplexNumber(2,4)
obj2=ComplexNumber(5,7)
print(obj1+obj2)
print(obj1-obj2)
print(obj1/obj2)
print(obj1==obj2)
print(obj1 != obj2)