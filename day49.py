 #in today class i will cover the diffrence between instance variable and class variables..

# when we make variable for whole class mean all will share that variable that is class variable
#class map the real world entity
#instance variable are associated with instance.
#first priorty is instance variable then check class variable.
class employe:
    school="National university of modern langues" #class variable that share with all..
    def __init__(self,name):
        self.name=name
        self.age=123
    def showMethod(self):
        print(f"Name is {self.name} and age is {self.age} and school is {self.school}")
emp1=employe("zack")
emp1.age=300  
emp1.school="Nust"              #instance variable 
emp1.showMethod()

emp2=employe("jack")
emp2.school="Behria"            #instance variable
emp2.showMethod()

emp3=employe("martin")
emp3.showMethod()  #now it will print only class variable becuase emp 3 dont have any instance of school 

# Consider a Car class with the following attributes:

# Class variable: total_cars (to keep track of the total number of cars)
# Instance variables: make (the make of the car), model (the model of the car), and fuel (the current fuel level in gallons).
# The class should have the following methods:

# __init__(self, make, model, fuel): Initializes the car with the given make, model, and initial fuel level. It should also update the total_cars class variable.

# get_info(self): Returns a string with information about the car, including make, model, current fuel level, and the total number of cars.

# Write the Car class with the described functionality and demonstrate its usage with at least two instances of cars.


class car:
    total_car=0
    def __init__(self,make,model,average):
        self.make=make
        self.model=model
        self.average=average
        car.total_car +=1

    def get_info(self):
        print(f"Car make is {self.make} car model is {self.model} and fuel average is{self.average} and no of totals car are {self.total_car}")

hunda=car("Honda","12Model","18km")
hunda.get_info()

suzuki=car("Suzuki","19Model","23km")
suzuki.get_info()

