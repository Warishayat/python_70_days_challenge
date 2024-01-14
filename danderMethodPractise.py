class student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def __str__(self):
        return f"name is {self.name} and rollnumber is {self.rollnum}"

waris=student("wariis","Sp-21368")
print(waris)

#   What is the difference between the __str__ and __repr__ methods?
#   Implement a class with both __str__ and __repr__ methods.
class university:
    def __init__(self,name,rollnum,depart):
        self.name=name
        self.rollnum=rollnum
        self.depart=depart
    def __repr__(self):
        return f"{self.name} and {self.depart} and rollhun is {self.rollnum}"
    
wariss=university("waris","Sp-21368","Software-Engineering")
print(repr(wariss)) 



#example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating an instance of the Point class
point = Point(3, 5)

# Printing using str() and repr()
print(str(point))  # Calls point.__str__(), output: "(3, 5)"
print(repr(point)) 