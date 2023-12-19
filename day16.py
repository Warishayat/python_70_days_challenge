#we pass arguments though the function and i will explore that today.

#positional arguments
def avg(a,b):
    print('The avg is',(a+b)/2)
avg(4,5) 



#default arguments
def avg(a,b=6):
    print('The avg is',(a+b)/2)
avg(30) 


# 1:these arguments are called default arguments:
#  2: keyword argument where argument order doesnot be change.
# 4: variable length arguments
#  3: v required arguments which are compuslory


#2:
def avg(a,b):
    print('The avg is',(a+b)/2)

avg(b=10,a=16)  #keyword arguments

#variable length arguments.
def average(*numbers):
    sum=0
    for i in numbers:
        sum= sum+i
        print('Aaverage is', sum / len( numbers ))
average(5,6)


# **keywargs arguments
def name(fname="Hayat",mname='Abbasi',lname="Waris"):
    print(f"My name is {fname} and middle name is {mname} and last name is {lname}")
name(lname="Saaaab")


#variable length arguments:#
def average(*numbers):      
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)  #return value back to the calling function
    print(type(numbers))

c=average(4,6,2)
print(c)


def values (**name):
    print(type(name))
    print("",name["name"],name['mname'],name['lname'])

values(name="kashan",mname="khan",lname="jameel")



