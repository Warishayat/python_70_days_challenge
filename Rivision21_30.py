#Today i will cover the formatting string..

name="waris"
Midname="Hayat"
LastName="Abbasi"

print(f"Name is {name} and mid name is {Midname} and last name is {LastName}")

# 2 question 
depart="Software-engineering"
rollnumber="Sp-21368"
Section="4A-Afternoon"

print(f"Department is {depart} and rollnum is {rollnumber} and section is {Section}")


#Doc_string
def average(a,b):
    '''this is he function which wil take the two paramater a and b
        and it will print the average function.
    '''
    result=(a+b)/2
    print("The result of average is:",result)

average(12,13)
print(average.__doc__)


#:Question2

def sum(a,b,c):
    ''' it is the function which take 3 parameter and print the sum of the
    result
    '''
    result=a+b+c
    print(f"The sum of the sum function is:",result)
sum(12,13,14)
print(sum.__doc__)

#now i will cover the set what is set and function of set..

l={1,2,3,4,5,6}
print(type(l))      #to find the type
l1={6,5,7,8,9,10}
#to find the intersection
print(l.intersection(l1))       #Make intersection between l1 and l
print(l.union(l1))              #Make union between l1 and l
print(l.difference(l1))         #l is hoow much diffrent from l1
print(l1.difference(l))         #l1 is hoow much diffrent from l
print(l.issubset(l1))
print(l.issuperset(l1))
print(l.pop())                  #it pop the random value from the set
l1={6,5,7,8,9,10,6}
print(l1)           #it will automaticaly remove the duplication from the set.
temp=list(l1)       #it will chage the type from set to list
print(type(temp))   #type of list
print(temp.append(12))
print(temp)
l1=set(temp)
print(type(l1))
print(l1.remove(10))           #it will remove the element 
print(l1)
print(l1.add(124))             #it will add a value
print(l1)

#Error handling
try:
    num=int(input("Enter the number:"))
    if num>0:
        print("Number is positive.")
    else:
        print("Number is negative:")
except ValueError:
    print("You do make some value error")


#Question2: tajke list and print the index error:
    
try:
    l=[1,2,3,5,6,7]
    idx=int(input("Enter the idx to get the value:"))
    result=l[idx]
    print(result)
except IndexError:
    print("You do make someindex error.")

#Question3: # Create a function that takes a list and an index as input and returns the element at that index.
# Handle both IndexError and TypeError gracefully.
def findElement(l,idx):
    try:
        result=l[idx]
        return result
    except IndexError:
        print("You do make some index error.")

l=[1,2,3,4,5,6,7,8,9,11,12]
try:
    idx=int(input("Enter the index to find element from the list:"))
    getresult=findElement(l,idx)
    print(getresult)
except ValueError:
    print("invalid literal for int() with base 10: 'waris'")

#for else keyword 
    
for _ in range(10):
    print(_,end=" ")
else:
    print("Else block after loop executed..")

#Question2: what if else will executed if we use break in loop.
for i in range(5):
    if i==4:
        break       #after that nothing will be executed.
    print(i)
else:
    print("i'll be print or not?")


#final keyword:

try:
    num=int(input("Enter number:"))
    print(num)
except ValueError:
    print("You do make somevalue Error.")
finally:
    print("i will execute in every condition.")

#Question2: # Write a Python program that reads a text file named "sample.txt" and prints the number of 
# lines in the file. If the file is not found, handle the exception and print an appropriate error message.
# Feel free to attempt these questions, and if you have any specific doubts or need help with solutions, feel free to ask!
try:
    with open ("sample.txt","r") as f:
        result="sample.txt".readline()
except FileNotFoundError:
    print("File NOt found")
finally:
    print("Everything is on track")

#Short hand if else/ternery operator //using shorthand tell num is even or odd
num=int(input("Enter the number:"))
print("Even Number:",num) if num%2==0 else print("Number Odd:",num)
    
#Question using short hand if else find the maximum number.
n=int(input("Enter number 1:"))
m=int(input("Enter number 2:"))
print("Num 1 is maximum",n) if n>m else print("Num 2 is maximum",m)

    
#Enumerates: (it will print the index of the loop)
list=[12,13,14,15,16,17,8,9,00]
for key,value in enumerate(list,start=1):
    print(f"{key} : {value}")

#question2:
def day(l):
    for idx,val in enumerate(days,start=1):
        print(f"{idx}:{val}")

days=['sunday','monday','tuesday','wednesday','Thurusday','Friday','Saturday']
day(days)

#import module
import math as m 
print(m.sqrt(25))
print(m.factorial(6))
print(m.exp2(4))
print(m.lcm(14))
print(m.pow(10,5))
print(m.floor(12))
print(m.log(5))

#dictionary
dict={
    "name":"python",
    "fee":21000, 
    "Duration":"3 months"
}
# print(dict.pop("fee"))          #fee will be deleted from the dict.
dict.update({"section":"4A-Afternoon"})
dict.update({"fee":30000})      #it will update the value
dict.clear()        #it will clear the list
for key,value in dict.items():
    print(f"{key}: {value}")


#nested dictionary:
dict2={
    'php':{"duration":"2month","fee":"20000"},
    'Cpp':{"duration":"3month","fee":"22000"},
    'python':{"duration":"3month","fee":"23000"},
    'Dsa':{"duration":"6month","fee":"24000"}
}
dict2["python"]["fee"]=60000    #updations
for key,value in dict2.items():
    print(key,value['fee'])
