#operator overloading

class numbers():
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"i is={self.i},j is={self.j},and k is={self.k}"
    def __add__(self,other):
        return f"Addition: {self.i+other.i} {self.j + other.j} {self.k + other.k}"
    #multiply the two instance variable using dunder method
    def __sub__(self,other):
        return f"Subtraction: {self.i-other.i} {self.j-other.j} {self.k-other.k}"

compl=numbers(12,13,14)
print(compl)
compl2=numbers(12,14,16)
print(compl2)
print(compl+compl2)
print(compl-compl2)
#question2 multiply the two instance variable using dunder method



#inheritance single inheritance
class university:               #parent class
    def __init__(self,name):
        self.name=name
    def __str__(self):
        print(F"name is {self.name}")

class student(university):          #child class
    def __init__(self,name,rollnum):
        super().__init__(name)
        self.name=name
        self.rollnum=rollnum
    def __str__(self):
        return(f"Name is {self.name} and rollnum is {self.rollnum}")

#instance will also make of child class
waris=student("waris","sp21368")
print(waris)


#Multiple iheritance multipt chld clas hold the same aprent class
class vehical :             #base class/parent class
    def __init__(self,make):
        self.make=make
    def __str__(self):
        return(f"Name is {self.make}")

class car():
    def __init__(self,year,wheel):
        self.year=year
        self.wheel=wheel
    def __str__(self):
        return(f"manufuctured year is {self.year} and wheel have {self.wheel}")
class bike(vehical,car):
    def __init__(self,make,year,wheel) :    #For vehical
        self.make=make
        self.year=year
        self.wheel=wheel
    def __str__(self):
        return (f"Make by {self.make}, Manufuctured year is {self.year} and wheel have {self.wheel}")
    
fortuner=bike("CD-70","2021","2")
print(fortuner)

#multilevle
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
waris=car("Waris-Hayat","Abbasi","Balack","Fortuner")
waris.display()

# #walrus
# print(name:=input("Enter your name: "))
# #take 2 number and tell which oneis maximum
# (num1:=int(input("Enter number1: ")))
# (num2:=int(input("Enter number2: ")))
# if num1>num2:
#     print("Num1 is maximum")
# elif(num2>num1):
#     print("Num2 is maximum")
# else:
#     print("Both are equal")

#genrator which genrate value on the fly
#even number
def evenNumber(list):
    for i in list:
        if i%2==0:
            yield i
l=[12,1,314,15,5,66,7,7,88]
result=evenNumber(l)
print(list(result))


#It will genrate thenumberon the fly.
def number(n):
    for i in range(n):
        yield i*2
n=number(10)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

# garbage collector

import gc
class student:
    def __init__(self,name):
        self.name="waris"
    def __str__(self):
        return f"name is {self.name}"
    def __del__(self):
        print( f"refernce has been {self.name} deleted...")
tabi=student("tabish")
print(tabi)
del tabi
gc.collect()        #manually call garbage collector


#threading
import threading
def evennumber(l,lock):
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
    with lock:
        print("list of even is:")
        print(even)
def oddnumber(l,lock):
    odd=[]
    for i in l:
        if i%2!=0:
            odd.append(i)
    with lock:
        print("list of odd is:")
        print(odd)
l=[1,2,3,4,5,6,7,8,9]
lock=threading.Lock()
t1=threading.Thread(target=evennumber,args=(l,lock))
t2=threading.Thread(target=oddnumber,args=(l,lock))

t1.start()
t2.start()

t1.join()
t2.join()

#multiprocessing

#by using multiprcoessing find the even and odd number from the list..
import multiprocessing

def Checkeven(n,lock):
    even=[]
    for i in n:
        if i%2==0:
            even.append(i)
    with lock:
        print(even)

def CheckOdd(n,lock):
    odd=[]
    for i in n:
        if i%2 !=0:
            odd.append(i)
    with lock:
        print(odd)
if __name__ == '__main__':
    list_number=[12,13,14,15,1,17,18,19]
    lock=multiprocessing.Lock()
    check_even=multiprocessing.Process(target=Checkeven,args=(list_number,lock))
    check_odd=multiprocessing.Process(target=CheckOdd,args=(list_number,lock))


    check_even.start()
    check_odd.start()

    check_even.join()
    check_odd.join()