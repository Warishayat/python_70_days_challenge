# Create a Calculator class with a static method named add_numbers that takes two numbers
#  as parameters and returns their sum. Additionally, create an instance method named multiply
#  that takes two numbers as parameters and returns their product. Test your class by performing
#  addition and multiplication operations.

class calculator:
    

    @staticmethod
    def sum(x,y):
        return x+y
    @staticmethod
    def product(x,y):
        return x*y
    
print(calculator.sum(12,13))
print(calculator.product(12,13))



# Create a Person class with the following attributes: name, age, and location. Implement
# a class method named create_person that takes values for name, age, and location as 
# parameters and returns an instance of the Person class with the specified attributes.
#  Additionally, implement an instance method named display_info that prints the 
#  person's name, age, and location.

class person:
    def __init__(self,name,age,location):
        self.name=name 
        self.age=age
        self.location=location
    @classmethod
    def create_person(cls,str):
        return cls(str.split(",")[0],str.split(",")[1],str.split(",")[2])
    def display_info(self):
        print(f"The name is {self.name} and age is {self.age} and location is {self.location}")

str="Waris_Hayat,22,islamabad_pakistan"
a=person.create_person(str)
a.display_info()