#encapsulation
class bank():
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance

    def displayINformation(self):
        print("Name is:",self.__name,"Blance is:",self.__balance)
    def getvalue(self):
        return self.__balance           #private variables
    def setvalue(self,new_balance):
        self.__balance=new_balance
person1=bank("waris",12000)
print("Value cannot chnage directy:",person1.getvalue())
person1.setvalue(14000)         #update the value
person1.displayINformation()


#Question2
# Design a Car class with the following requirements:

# The class should have private attributes for the car's make, model, and year.
# Implement getter methods for the make, model, and year attributes.
# Implement a setter method for the year attribute with the following validation:
# The year should be a positive integer.
# Implement a method called display_info that prints out the car's information in a user-friendly format.
class car():
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year
    def displayinformation(self):
        print(f"make is {self.__make},model is {self.__model} and year is {self.__year}")
    def getvalue(self):
        return self.__make
    def setvalue(self,newMake):
        self.__make=newMake
waris=car("hunda",22,21)
print("You can only change Make of the company.")      #only this can be change
waris.setvalue("Hero")     #it will never change the value because refrence variables are private.
# waris.__year=3022 these value will never change directly.
# waris.__model=34
waris.displayinformation()


#class inherit:
 
class university():     #parent class
    print("This is parent class")

class studet(university):           #child class
    print("this is child class which inherit the university which is main class.")

a=studet()              #object and instance f the class


#Question2: 

class parent():
    def __init__(self):         #parent class
        self.name="waris"
    def displayinformation(self):
        print(f"Name is {self.name}")

class child(parent):
    def __init__(self):
        self.depart="Software Engineering"
    def displayinformation(self):
        print(f"depart is {self.depart}")

childinstance=child()
childinstance.displayinformation()

#pricate public and protected specifiers

class atm():
    def __init__(self):
        self.name="Allied atm"              #public specifiers
        self._pin=12300                     #protected
        self.__balnce=3000                     #private
    
allied=atm()
print("The atm name is:",allied.name)                  #it will be accesable outside from the class
print("The atm pin is:",allied._pin)                  #it will be acessable from outside from the class.
print("The balace is:",allied._atm__balnce)              #it will never acess from outside the class for this we use name mangling


#Question 2 for acess specifiers

class girl():
    def __init__(self):
        self.beauty="Nil"                   #public 
        self._name="Nora fatehi"            #protected
        self.__number=23928398              #private 
    
    def display(self):
        print(f"name is {self._name},about beauty is {self.beauty} and number is {self.__number}")

nora=girl()
nora.display()
# print(nora.__number)            #it will never acess


#static method that donot hove any link with instance of the class and it does not need of any self eyword.

class student:
    def __init__(self):
        self.number=11
        self.number2=22

    def displayNumber(self):
        print(f"Number are {self.number} and {self.number2}")
    @staticmethod
    def multiplay(n,m):
        print("The Multiply of Num1 and Num2 is:",n*m)
    @staticmethod
    def add(n,m):
        print("The add of Num1 and Num2 is:",n+m)

math=student()
math.displayNumber()
student().multiplay(12,14)
student().add(12,14)



#instance variable and class variable
#always first priority is instance variable when instance is not avialable then will gave preferance to class variable

class university():
    university="National University of modren languages"            #class variable
    def __init__(self):
        self.rollnum="Sp21368"
    def info(self):
        print(f"Rollnum is {self.rollnum} and university is {self.university}")
waris=university()
waris.university="University of munich germany"
waris.info()

waris2=university()
waris2.info()


#class method that is bound eith the class.

class data():
    name="Waris - Hayat - Abbasi"           #class variable
    def __init__(self):
        self.rollnum="Sp21368"
    def display(self):
        print(f"Name is {self.name} and rollnum is {self.rollnum}")

    @classmethod
    def changeclass(cls,newname): #it take first variabe as a classl and then newreferance value
        cls.name=newname

waris=data()
waris.changeclass("Waris_Hayat_Abbasi")
waris.display()


#Alternate constructor;

class univers:
    def __init__(self,name,rollnum,depart):
        self.name=name
        self.rollnum=rollnum
        self.depart=depart
    def information_universe(self):
        print(f"Name is {self.name}, rollnum is {self.rollnum} and depart is {self.depart}")
    @classmethod
    def variableclass(cls,str):
        return cls(str.split(",")[0],str.split(",")[1],str.split(",")[2])       #spilit where coma use

str="waris Hayat Abbasi,Sp21368,Software-engineering from ghaxali"
waris=univers.variableclass(str)
waris.information_universe()


#dir dict and help

class person:
    def __init__(self,name,section):
        self.name=name
        self.section=section
    def displayInfo(self):
        print(f"This is {self.name} and his/her section is {self.section}")
waris=person("waris","4Aa-afternoon")
# 
#SuperKeyword
print(waris.__dict__)           #identify the attribute of the classs
# print(help(person))       #help to recoginize about the class.
# print(dir(person))      #it tell us about method.

class university():
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name is {self.name}")
class student(university):
    def __init__(self,name,rollnum):
        super().__init__(name)          #use to call main/parent class construcotr
        self.name=name
        self.rollnum=rollnum
    def display(self):
        super().display()       #Use to call main/parent class ethod
        print(f"The name is {self.name} and rollnum is {self.rollnum}")
numl=student("waris",21368)
numl.display()


#method overloading

class data():
    def __init__(self,name,rollnum,sec):
        self.name=name
        self.rollnum = rollnum
        self.sec=sec
    def information(self):
        print(f"Name is {self.name} ,rollnum is {self.rollnum} and sec is {self.sec} ")
class disbale(data):
    def __init__(self,name,rollnum,sec,disablity):
        super().__init__(name,rollnum,sec)
        self.name=name
        self.rollnum = rollnum
        self.sec=sec
        self.disablity=disablity
    def information(self):          #method override
        print(f"Name is {self.name} ,rollnum is {self.rollnum} and sec is {self.sec} and disability is {self.disablity} ") 

person1=disbale("shani","1232","A morning","Nil")
person1.information()
person2=disbale("waris","1238","A morning","Nil")