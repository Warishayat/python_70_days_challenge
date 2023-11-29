##all these are comment which are mentioned below:-
##in this part we will cover he basic things about the python like basic cli,comments,indentation
##variables,keyword in python,datatypes,ascii and unicode,taking input from user
##operators, float to int ,int to float (type casting etc)
##hirarchery

print("Hellow \nworld!")                ##\n to start a new line:

#variables and their declaration: variable are container which are used to store data
#variables always stat with name without builtin word varaible name cant be stat with number like 1abc,
#we can make the variable name like var_1 s1 etc it canot start with special character like #sum.
#python keywords which are alreday define we cant use as a variable name:
a=10
b=20
c=a+b
print("The value of C is",c)

                    #we can also override the same variables:
x=10
x=12
print("The value of X is override",x)

#now we talk about types string,int ,float,bolean values:
n="Waris_Hayat"
print(type(n))              #this type word will define the type of variable:
i=10                        #int data types
print(type(i))
j=10.2                       #float data types
print(type(j))
is_student=True
print(type(is_student))       #bolean value
#if i want to print all these value combine than i wil simply do:
print(f"my name is={n} my integer value is ={i} my float value is ={j} my bolean value is={is_student}")
print("My string value has been changed "+n + " abbasi")             #we can cnhage the value same like this:
print("My integer value also has been changed",i+ 30)
print("My float value also has been changed",j+ 30.5)
#seprator
print(n, i, j, is_student, sep="->") 