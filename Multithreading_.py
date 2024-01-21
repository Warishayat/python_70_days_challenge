import threading
def Evennumber(n):
    for i in range(n):
        if i % 2==0:
            print(f"Even Number:-",i)

def oddNumber(n):
    for i in range(n):
        if i % 2 != 0:
            print("Odd Number:-",i)
    
Evennumber(10)
oddNumber(10)
Even_number=threading.Thread(target=Evennumber,args=[10])
odd_Number=threading.Thread(target=oddNumber,args=[10])

Even_number.start()
odd_Number.start()

Even_number.join()
odd_Number.join()


#By using multithreading find the alphabat and alphanumeric in the list .....

import threading
def alphanumeric(num):      #to check alpha in list
    alpha=[]
    for i in num:
        if isinstance(i,str):
                if i.isalpha():
                    alpha.append(i)
    print("Alphanumeric values are",alpha)


def Digit(num):
    digit=[]            #to store digit in the new list from the list
    for i in num:
        if isinstance(i, (int,str)):
            for char in str(i):
                if char.isdigit():
                    digit.append(char)
    print("Alphanumeric values are",digit)

list=[12,"waris","Abbasi","Google",15,1,"MICROSFOT"]
numeric=threading.Thread(target=alphanumeric ,args=[list])

Digit_=threading.Thread(target=Digit ,args=[list])

#to start the threads
numeric.start()
Digit_.start()

numeric.join()
Digit_.join()