#Today i revise the tpoic from 31 to 35.

#Global variable and local variables global variables are declared Globally where the local
#variables declared inside the function when gone executed variable gone destroyed

x="Waris"
def greet():
    x="Waris-Hayat"     #it will never change the value of global variable.
    print("Hellow world.")  
    print(x)            #local varibale                    
greet()                     #function call     
print(x)                    #it will print Global value.

#but if we want to change the global value inside function we use Global keyword
print("New program are here.....")

name="Waris"
def greetName():
    global name    #Now it will never change the value of global variable.
    name="Waris-Hayat-Abbasi"  
    print(name)            #Now its global varibale                    
greetName()                     #function call     
print(name)                     #it will print the chnage value of global


# if vs ==
a=4
b='4'
print(a==b)                 #False
print(a is b)               #False

l=[12,1,314,14]
l2=[12,1,314,14]
print(l==l2)            #it compare values
print(l is l2)          #it compare adress


a=4
b=4
print(a is b)       #true
print(a == b)       #true


#class 
class student:
    name="waris"
    print(name)
a=student()
#class 2
class university:
    def __init__(self,):
        print("Univeristy is numl")
waris=university()


#class constructor and object

class student:
    def __init__(self,name,depart): #constructor 
        self.name=name
        self.depart=depart
        print(f"name is {self.name} and depart is {self.depart}")

waris=student("waris","Software-Engineering")       #object


