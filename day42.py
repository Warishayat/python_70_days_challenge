#today i will cover class object and constructor:

class info:  # here we make class with name info with keyword class:

    def __init__(self, name, claas,): #Here we make a constructor which is permaterized
        self.name=name
        self.claas=claas

    def getinfo(self):  #Here i make a function with name getinfo
                print(f"my name is={self.name} and my class is={self.claas}")

person1=info("waris","software_eng") #creation object 1 by passing value 

person1.getinfo() #call the function1 for object 1(person==1)

person2=info("bilal","software_eng") #creation object 2 by passing value

person2.getinfo() #call the funtion1 for object 2(peson==2)




#now i will make default construcotr:

class railway:
    name="Greenlane"
    ticket_price="400"
    destinantion="lahore"
    time="8-hours"

    def __init__(self): #this is deault constructor with no any argument:(where self tell us aboutmethod which method is calling;)
        print("Hey i am default ocnstruototor im going to run with creating object")


person1=railway()
person2=railway()
