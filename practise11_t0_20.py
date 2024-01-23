#Topic today i will cover:

#ternery opereator
num=int(input("Enter the Number."))
result ="even" if num %2==0 else "odd"
print(result)

#2 check the given number is negative or positive.
num=int(input("Enter number:"))
number='positive' if num>0 else "negative"
print("The number is:",number)

#3 check two num which is maximum
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
result="Num1 is maximum" if num1>num2 else "Num2 is maximum"
print(result)

###loops

for i in range(1,10,1):
    print(i,end=" ")

#while loops
print()
i=1
while(i<10):
    print("Hellow_World",end=" ")
    i+=1

#iterate the loop on the string
print()
name="Waris_Hayat_Abbasi"
for i in name:
    print(i,end=" ")


#iterate the loop on the list
print()
student=[1,2,"waris",4,8,64,3,2]
for i in student:
    print(i,end=" ")

#Question : print the even number between initialized and end point?
print()
initial=int(input("Enter the first point:"))
final=int(input("Enter the final point:"))

i=initial
while(i<final):
    if i%2==0:
        print(i,end=" ")
    else:
        pass
    i+=1
    
#break and continue statments:

for i in range(10):
    if i ==5:
        continue        #5 would skip and print all the loop
    else:
        print(i)

#2 when you got a then skip that word from the string
print()
name="waris_Hayat_Abbasi"
for i in name:
    if i=='a':
        continue
    else:
        print(i,end="")
        
#3 list=[10,12,13,14,15,16,17] find 17 then skip
print()
list=[10,12,13,14,15,16,17]     
for i in list:
    if i==17:
        continue
    else:
        print(i,end=" ")

        
#3 list=[10,12,13,14,15,16,17] find 13 then break
print()
list=[10,12,13,14,15,16,17]     
for i in list:
    if i==13:
        break
    else:
        print(i,end=" ")

#2 when you got b then break loop
print()
name="waris_Hayat_Abbasi"
for i in name:
    if i=='b':
        break
    else:
        print(i,end="")
        
#find 5 then brake
print()
for i in range(10):
    if i ==5:
        break        #5 would skip and print all the loop
    else:
        print(i,end="")

#def function
print()
def sum():
    print("This function is doing sum.")
sum()

#function with parameter
print()
def sum(a,b):
    sum =a+b
    print("This function is doing sum.and sum value is :",sum)
sum(13,14)
#

#argumets type

def sum(a,b):       #positional arguments
    result=a+b
    print("The result is:",result)
sum(12,14)

#2 default argumnets

def add(a,b=12):        #default arguments
    result=a+b
    print("The result of default arguments is:",result)
add(12)

#3 keyword arguments

def detail(name,lastname):
    print(f"Name is {name} and last name is {lastname} ")
detail(name="waris",lastname="Hayat")


#variable length arguments
def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print("The average is:",sum/len(number))
average(4,5,6,)

#keywords arguments:

def persondetail(**detail):
    print("",detail ['name'],detail["classs"],detail["depart"])

persondetail(name="waris",classs="42-number",depart="Software-engineering")

#2
def studentDetail(**detail):
    print("",detail["name"],detail["Midname"],detail['Lastname'])

studentDetail(name="Waris",Midname="Hayat",Lastname="Abbasi")


#list
list=[12,13,14,15,16,17,18,19,20,12]
print(type(list))
print(len(list))
list.append(8)
print(list)
print(list.pop())
print(list[9::-5])
# print(list[::-1])
print(list[0:5:1])
print(list[-5::-1])
print(list.remove(16))
print(list)
print(list.index(18))
print(list.count(12))
print(list.reverse())

list2=["waris",12,1314,14,15,16,17,18]
if "waris" in list2:
    print("True")
else:
    pass
list3=[i for i in range(10)]    #list comprehension
print(list3)
list4=[i for i in range(10) if i%2==0]
print(list4)
print(list4.sort(reverse=True))
print(list4)
print(list4.sort())
print(list4)
list5=list3+list4   #list concatination
print(list5)
list5[0]=111
print(list5)
print(list5.remove(111))
print(list5)


#tuple
tep=(1,2,3,7,5,6,7,8,9,10,12)
print(len(tep))
print(type(tep))
print(tep.count(3))
print(tep.index(3))
print(12 in tep)
print(13 in tep)
tep2=(12,13,14,15,16,17,18)
tep3=tep+tep2
print(tep3)
print(tep[::-1])
print(tep[-7::-1])
print(tep3)
if 13 and 14 and 17 in tep3:
    print("These are found:")
else:
    print("No found")
tep=(1,2,3,7,5,6,7,8,9,10,12)
print(tep)
temp=list(tep)
print(temp)
temp.append(12)
print(temp)
print(temp.count(12))
print(temp.pop())
print(temp.remove(8))
print(temp)
print(temp.index(5))
print(temp.reverse())
print(temp)
tup=tuple(temp)
print(tup)
print(tup)