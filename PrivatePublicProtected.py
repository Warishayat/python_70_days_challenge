# Create a class named Person with the following attributes:

# Public attribute: name
# Protected attribute: _age
# Private attribute: __address
# Implement methods to get and set values for each attribute.
#  Create an instance of the class and demonstrate the use of these methods


class person:
    def __init__(self,name,age,adress):
        self.name=name
        self._age=age
        self.__adress=adress

    #getmethod calling
    def getmethod(self):
        return self.name,self._age,self.__adress
    
    #now set method to set the new values:
    def Setmethod(self,New_age,New_adress):
        self._age=New_age
        self.__adress=New_adress

xyz=person("babbar",19,"india-colkata")
print(xyz.name,xyz._age,xyz._person__adress)

print()

xyz.Setmethod(21,"Jehlum")
print("The value after updation:")
print(xyz.name)
print(xyz._age)
#name_mangling
print(xyz._person__adress)


