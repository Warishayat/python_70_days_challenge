#today i will cover what is class how to make cass and inherit class?

class student:                          	            #parent class
    def __init__(self ,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def displayinfo(self):
        print(f"The student against {self.rollnum} is {self.name}")


class university(student):                              #child class
    def __init__(self,name,rollnum,department,degree):
        super().__init__(name,rollnum)
        self.department=department
        self.degree=degree
    
    def show(self):             #by super keyword we acess main class method
        super().displayinfo()
        print(F"Their degree is {self.degree} while depart is {self.department}")
    

student1=university("waris Hayat",21368,"Ghazali-Block","Software-engineer")
student1.show()

# #example
# Question: Create a Vehicle class as the parent class with the following attributes and methods:

# Attributes:

# make (str): The make of the vehicle.
# model (str): The model of the vehicle.
# year (int): The manufacturing year of the vehicle.
# Methods:

# __init__(self, make, model, year): A constructor to initialize the attributes.
# display_info(self): A method to display information about the vehicle in the format "Make: [make], Model: [model], Year: [year]".
# Next, create a child class Car that inherits from the Vehicle class with an additional attribute:

# Attributes:
# 4. num_doors (int): The number of doors on the car.

# Methods:
# 3. __init__(self, make, model, year, num_doors): A constructor to initialize the attributes of both the parent and child classes.

# display_info(self): Override the display_info method in the child class to include the number of doors.

class vehical:
    def __init__(self,companny,model,year):         #constructor
        self.companny=companny
        self.model=model
        self.year=year
    def display_info(self):                           #method
        print(f"Company:{self.companny}, Model={self.model},Manufuctured_Year:{self.year}")



class car(vehical):
    def __init__(self,companny,model,year,num_doors): #comstructor
        super().__init__(companny,model,year)         #main class attribute inheit by super keyword
        self.num_doors=4
    
    def display_info(self):
        super().display_info()
        print(f"Company:{self.companny}, Model={self.model},Manufuctured_Year:{self.year},No-of-Doors:{self.num_doors}")
        

range_rover=car("Honda","2024","2023","4")
range_rover.display_info()