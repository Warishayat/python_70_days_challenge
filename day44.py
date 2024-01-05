#getter and setter
# in today class i will cover the getter and seter 
#its  also called encapsuation.its mean some thing private you cant change.
class studet:

    __name="hellow"                 #(__) is for making something private


    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(Self):                #private function
        print("welcome to the ws cube tech")


obj=studet()                    #obj is the instance of the class student



# Design a BankAccount class with the following requirements:

# The class should have private attributes for the account holder's name and account balance.
# Implement a getter method for both the name and balance attributes.
# Implement a setter method for the name attribute with the following validation:
# The name should be a non-empty string.
# Implement a setter method for the balance attribute with the following validation:
# The balance should be a non-negative float.

class bank:

    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    
    #get methof to get the value
    def GetValue(self):
        return self.__name,self.__balance
    
    #now set the new value to name and age
    def Setvalue(self,new_name,new_balance):
        self.__name=new_name
        self.__balance=new_balance

person=bank("waris",220000)

name,balance=person.GetValue()
print("name:",name)
print("Balance is:",balance)

person.Setvalue("Waris Hayat",55555555555555)
new_name,new_balance=person.GetValue()
print("UPDATED name:",new_name)
print("UPDATED Balance is:",new_balance)





# Design a Car class with the following requirements:

# The class should have private attributes for the car's make, model, and year.
# Implement getter methods for the make, model, and year attributes.
# Implement a setter method for the year attribute with the following validation:
# The year should be a positive integer.
# Implement a method called display_info that prints out the car's information in a user-friendly format.


class car:
    def __init__(self,name,year):
        self.__name=name
        self.__year=year

    def displayinfo(self):
        print(f"This car name is{self.__name} and year manufutured is:{self.__year}")

    def GetterMethod(self):
        return self.__name,self.__year
    
    def SetterMethod(self,Nname,Nyear):
        self.__name=Nname
        self.__year=Nyear
    
    def carinfo(self):
        print(f"The car has name {self.__name} and year manufuctured have {self.__year}")

supra=car("Supra",2023)
name,year=supra.GetterMethod()
print("Car name:",name)
print("year manufuctured",year)
supra.carinfo()                             #call the function

supra.SetterMethod("Range Rover",2023)
Nname,Nyear=supra.GetterMethod()
print("New Updated car:",Nname)
print("New Manufuctured year:",Nyear)