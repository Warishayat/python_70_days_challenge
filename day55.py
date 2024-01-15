#method overriding
#when we want to make the same name function in diffrent class and inherit then most recent child class will
#automaticaly overirde the all function that have the same name like this.
#Method over riding

class student:
    def __init__(self):
        self.name="Waris-Hayat"
        self.rollnum="SP-21368"
        self.section="4A-Afternoon"
    def __str__(self):
        return f"Name is {self.name} and class is {self.rollnum} and section is {self.section}"
    
class University(student):
    def __init__(self):
        super().__init__()
        self.teacher_name="Syed Taha"
        self.marks="3.8CGPA"
    def __str__(self):              #Method will override here
        return f"Name is {self.name} and rollnum {self.rollnum} and section is {self.section} teacher name is{self.teacher_name} and total marks are {self.marks}"
waris=University()
print(waris)
    

#Consider a base class Vehicle with a method fuel_efficiency() that calculates and 
# returns the fuel efficiency of the vehicle. Create two subclasses Car and Motorcycle
# that inherit from Vehicle. Override the fuel_efficiency() method in both subclasses to 
# provide specific implementations for cars and motorcycles. Additionally, create instances
# of both subclasses and demonstrate the use of the overridden method.

class vehical:
    def __init__(self):
        self.feulEfficeny=10.5
    
    def fuel_efficiency(self):
        return self.feulEfficeny 
    
class car(vehical):             #class car which inherit vehical
    def __init__(self):
        self.feulEfficeny=10.9
    def fuel_efficiency(self):
        return self.feulEfficeny
    
class motercycle(vehical):      #class motercycle which inherit vehical
    def __init__(self):
        self.feulEfficeny=10.1
    def fuel_efficiency(self):
        return self.feulEfficeny


moto=car()
print("The fuel efficency of moto:",moto.fuel_efficiency())
biker=motercycle()
print("The fuel efficency of moto:",biker.fuel_efficiency())




#Design a system for managing a library with books and magazines. Create a base class
# Publication with attributes such as title, author/editor, and publication year. Implement
# two subclasses: Book and Magazine. Override the display_info() method in both subclasses 
# to provide a detailed display of information for books and magazines. Additionally, create 
# instances of both subclasses, add them to a library collection, and demonstrate the use of 
# the overridden method.


class Publication:
    def __init__(self):
        self.title="Tom and Jerry"
        self.author="Waris-Hayat"
        self.pub_year=2024
    def display(self):
        return f"The title is {self.title},Author is {self.author} and public year is {self.pub_year}"
    
class Book(Publication):
    def __init__(self):
        self.title="Tim & Hortan"
        self.author="Asif Hayat"
        self.pub_year=2022
    def display(self):
        return f"The title is {self.title},Author is {self.author} and public year is {self.pub_year}"

class magazines(Publication):
    def __init__(self):
        self.title="Python 360"
        self.author="Waris"
        self.pub_year=2024
    def display(self):
        return f"The title is {self.title},Author is {self.author} and public year is {self.pub_year}"

mag=magazines()
print(mag.display())
note_Book=Book()
print(note_Book.display())