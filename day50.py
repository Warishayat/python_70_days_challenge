# #class method()...................
# that is bound the calss not the instane of the class

class student:
    comp="University of Oxford"

    def selfinfo(self):
        print(f"The name is {self.name} and compnay is {self.comp}")
    @classmethod
    def company(cls,newCompany):
        cls.comp=newCompany
a=student()
a.name="waris"
a.company("Tesla")
a.selfinfo()
print(student.comp)




# Imagine you are developing a simple banking system. Create a BankAccount class
#  with the following attributes:

# balance (initially set to 0)
# interest_rate (a class variable set to 5%)
# Implement the following methods:

# A constructor (__init__) that takes an initial deposit and sets the balance accordingly.
# A method calculate_interest(cls, amount) that calculates and returns the interest on a 
# given amount based on the class interest rate.
# A method deposit(self, amount) that adds the given amount to the account balance.
# A method withdraw(self, amount) that subtracts the given amount from the account balance.
# Feel free to add any additional methods or attributes you find necessary. Once 
# you've implemented the class, create an instance of it, perform some transactions,
# and demonstrate the usage of the class method to calculate interest




class Bank:
    intrest_rate=0.5
    def __init__(self,balance):
        self.balance=balance
    def deposite(self,amount):
        self.balance=amount
        print("Deposite Amount is:",amount)
        print("New Balance is:",self.balance)
    def withdrwal(self):
        cash=int(input("Enter the cash:"))
        if cash > self.balance:
            print("You cantnot withdraw more then you current amount")
            print("Your current amount is:",self.balance)
        else:
            self.balance=self.balance-cash
            print("Withdrawl SUCCESFULL!!!! New balane is :",self.balance)
    def interestSet(cls,NewInterst):
        cls.interest_rate=NewInterst
        result = cls.balance/100*cls.interest_rate
        print("The INTERSET IS :",result)
    

a=Bank(0)
a.deposite(50000)
a.withdrwal()
a.interestSet(0.7)