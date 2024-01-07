#private protected and public speifiers
#in python there is no any concept of private public and peotected specifir bbut these are covention



#by default all variable are public in python

class student:
    def __init__(self):
        self.name="waris"
        self.roll="sp-21368"

tabii=student()
#now i can acess from outside of the class 
print(tabii.name)
print(tabii.roll)


#private  variable which can not be accesable from the class directly but indirectly.
class car:
    def __init__(self):
        self.__name="Fortuner legender"
        self.__year=2024


vehical=car()
print(vehical._car__name) #but now it will not be accesable--->(Name-mangling)
print(vehical._car__year)


#protected specifiers(these all are just conventions)

class studets:
    def __init__(self):
        self._name="Coding is fun"
    
    def _funnanme(self):            #protected method
        return "Coding is fun"


class subject(studets):             #main class inherit here

    pass
obj=studets()
obj1=subject()

print(obj._name)
print(obj._funnanme())

#calling by object of subject class...
print(obj1._name)
print(obj1._funnanme())


