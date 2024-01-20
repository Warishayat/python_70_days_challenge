#garbage collector
import gc
class student:
    def __init__(self,name):
        self.name=name
        print("This is construtor :",self.name)
    def __del__(self):          #This will delete the object when del keyword is calling
        print("Distructor.",self.name)

student("zack")
print("Processing system")
a=student("object1")
print(a)
b=student("object2")
print(b)
del a   #destrucor call and delet object 1
del b   #destrucor call and delet object 2
print("process end")
 


#property that call destructor when program execution gone end garbage collector call destructor 
#and destroy the objects;
#1: instance/Refrance will be destroyed first.
#2: in second step object will be orphan (orphan object)
#3  then garbage collector take orphan object and call the destructor and destroy all the objects and clean the system.


#anaonmous object in python
#  refrence<----x=delta()--->deta is object
#when no referance become present thats called anonmous object






import gc

class ResourceHolder:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        print(f"ResourceHolder for {self.resource_name} created.")

    # def __del__(self):
    #     print(f"__del__ method called for {self.resource_name}. Resource released.")



a=ResourceHolder("defaulted")
print("ResourceHolder instance has been creatd")
# del a
gc.collect()