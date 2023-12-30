


# # ** 1:Filter out even numbers from a list using filter() and a lambda function.

# l=[1,2,3,4,5,6,7,8,9,10]
# EvenNumber=list(filter(lambda x:x%2==0,l))
# print(EvenNumber)


# # 2:: **Filter out strings with length less than 5 from a list of strings using filter() and a lambda function.

ListString=["waris","GoodNight","Hellow"]
LengthFinder=list(filter(lambda x:len(x)<5,ListString))
print(LengthFinder)

# 3: **Filter out prime numbers from a list using filter() 
# and a function to check for primality.
# demo=[1,2,3,4,5,6,7,8,9]
# def isprime(num):
#     if num<2:
#         return False
#     else:
#         for i in range(2,num,1):
#             if num%i==0:
#                 return False
#             return True

# CheckFilter=list(filter(isprime,demo))
# print("The new list of prime numbers are:",CheckFilter)



 # **Filter out elements containing the letter 'a' from a list of strings using filter() and a lambda function.

Elementlist=["Hellow","World","waris","Aabbasi"]
checkA=list(filter(lambda x:'a' in x,Elementlist))

print(checkA)

# **Filter out elements greater than 100 from a list of numbers using filter() and a lambda function.

NEW_LIST=[12,14,15,101,16,17,188,188,1000,17318,12,1434,3,566,88]

Element_Greater_Then_100=list(filter(lambda x: x>100,NEW_LIST))

print("The element in the list are greater then 100 are:",Element_Greater_Then_100)
