# Create an EmployeeData class with the following specifications:

# Private attributes: __salary
# Protected attribute: _employee_id
# Public attributes: name
# Implement the following methods:

# get_salary(): Returns the salary.
# set_salary(new_salary): Updates the salary but does not allow it to be lower than the existing salary.
# get_employee_id(): Returns the employee ID.
# set_employee_id(new_id): Updates the employee ID if it's a positive numb2
# er.


class EmployeeData:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self._employee_id=employee_id
        self.__salary=salary
    

    def get_salary(self):
        print(f"your salary is:{self._EmployeeData__salary}")

    def set_salary(self):
        new_salary=int(input("Enter the new salary:"))
        if new_salary <= int(self.__salary):
            print("Salary cannot be set at low:")
        else:
            self.__salary=new_salary
            print("Congratulation your new salary is:",self._EmployeeData__salary)
    def get_employee_id(self):
        print(f"Employe id:{self._employee_id}")
        
    def set_employee_id(self):
        id_get=int(input("pass the new id:"))
        if id_get<=0:
            print("Sorry Id cant be zero:")
        else:
            self._employee_id=id_get
            print(f"Your new employe id is: {self._employee_id}")
    

client=EmployeeData("kashif","109","700000")
try:
    choose=int(input("""
    What you wan to do:
    1: for get salary
    2: for set salary
    3: for get employe id
    4: for set employe id \n
    """))

    if choose==1:           #get salary
        client.get_salary()
    elif choose==2:         #set salary
        client.set_salary()
    elif choose==3:         #get employe id
        client.get_employee_id()
    elif choose==4:         #set employe id
        client.set_employee_id()
    else:
        print("ïnvalid character:")
except ValueError:
    print("ValueError: you make some ValueError.")