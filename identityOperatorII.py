#QUESTION:Define two lists, list1 and list2, with the same elements.
#Use the identity operator to check if list1 is the same object as list2. Print the result.

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10]

result = list1 is list2
print(result)