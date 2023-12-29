# Write a lambda expression that takes two parameters x and y and returns their sum.

sum=lambda x,y : x+y
print("The value of sum is:",sum(12,14))

# Filtering with Lambda:
# Given a list of numbers, use the filter function and a lambda expression
# to filter out the even numbers from the list.

l=[1,2,3,4,5,6,7,8,9,10]
even_number=list(filter(lambda x: x%2==0,l))
print(even_number)



#3
people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 28)]

Sorrt=sorted(people,key=lambda x:x[1])

print(Sorrt)


#Combining Multiple Lists with Lambda:
#Given two lists of numbers, use the map function and a lambda expression to add
#corresponding elements of the two lists.

l1=[1,2,3,4,5,6,7]
l2=[8,9,12,13,14,16]

addlist=lambda x,y :x+y

list3=list(map(addlist,l1,l2))

print("The thir list is:",list3)



# Using Lambda in List Comprehension:
# Create a list of squares of numbers from 1 to 10 using list comprehension
# and a lambda expression.


l=[i for i in range(10)]
print(l)

square=list(map(lambda x:x**2,l))

print(square)


#Calculating Average with Lambda:
# Given a list of numbers, use the reduce function and a lambda expression
# to calculate the average of the numbers.

from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
Calculate_average=reduce(lambda x,y:x+y,l)/len(l)

print(Calculate_average)
