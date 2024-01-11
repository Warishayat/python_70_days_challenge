# Consider a BankAccount class that represents bank accounts. Each account has an account
# holder, an account balance (initially set to 0), and an interest rate
# (common to all accounts). Implement the BankAccount class with appropriate instance 
# and class variables, and provide a class method to update the interest rate for all accounts.

class Bank:
    intrest_rate=0.5
    print("The old interst rate is",intrest_rate)
    def __init__(self,acc_holder_name,balance=0):
        self.acc_holder_name=acc_holder_name
        self.balance=balance
    def displayInformation(self):
        print(f"Acc holder name is {self.acc_holder_name} and balance is {self.balance} and interst rate is {self.intrest_rate}")
    @classmethod
    def update_intrest_dis(cls,NewInterstrate):
        cls.intrest_rate = NewInterstrate

perosn1=Bank("Zack") #balamce cen be initially zero but i set the 12344
perosn2=Bank("Martin","50000") ##balamce can be initially zero but i set the 50000
perosn1.update_intrest_dis(7)       #now it will update the intrest rate
perosn1.displayInformation()
perosn2.displayInformation()