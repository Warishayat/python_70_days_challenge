
# Create two classes, Person and Employee. The Person class should have attributes for
#  name and age, and a method display_info() that prints the name and age of the person
#  . The Employee class should inherit from Person and have additional attributes 
#  for employee_id and salary. Implement a method display_employee_info() in the
#   Employee class that displays information about the employee, including the
#    inherited attributes from the Person class.
# Instantiate an object of the Employee class and demonstrate the use of both display_info() 
# from the Person class and display_employee_info() from the Employee class.

class person:
    def __init__(self):
        self.name="waris"
        self.age="22"
    def displayinfo(self):
        print(f"This is {self.name} and his age is {self.age}")

class employe (person):
    def __init__(self):
        super().__init__()
        self.employe_id=101
        self.employeSalery="2 Cpa"

    
    def display_employee_info(self):
        super().displayinfo()
        print(f"Name is {self.name} Employe id is {self.employe_id},his age is {self.age} and his salery is {self.employeSalery}")

a=employe()
a.display_employee_info()