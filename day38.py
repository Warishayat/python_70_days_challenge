#map filterr and reduce
# it can take function as an arguments:

def cube(x):
    return x*x*x

print(cube(2))



l=[1,2,3,4,5,6,7,8,9]
print("Old list is:",l)
result=list(map(lambda  x:x*x*x,l))

print("The cube list is:",result)



#filter function
def filterfunction(a):
    return a > 4

finalResult=list(filter(filterfunction,l))

print("The filter function work as",finalResult)


#reduce method

from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9]

def sumNumber(x,y):
    return x+y

LastResult=reduce(sumNumber,numbers)

print("The last result of reduce will be=",LastResult)

#basic question are attahed to the newfile ======> mapFilterReduce.py