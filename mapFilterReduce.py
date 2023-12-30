# **Multiply each element of a list by 2 using map() and a lambda function.
# Question1:
lst=[1,2,3,4,5,6,7,8]
multiply=list(map(lambda x: x*2,lst))
print("After multipy of each element with 2 is=",multiply)


# Question2
# **Convert a list of strings to lowercase using map() and the str.lower function.
lst2=["PAKISTAN","GERMANY","ITALY","USA","UNITED-KINGDOM"]
convertLower=list(map(lambda x:x.lower() ,lst2)) #we pass function as an arguments and we pass list
print("All Upper case Convert into lower case",convertLower)


# Question3
# **Square each element of a list using map() and a lambda function.
list3=[12,13,14,15,16,17] #list
Squre=list(map(lambda x:x**2,list3))
print("The squre of the elements are:",Squre)

# Question4:
# **Concatenate each string in a list with a specific character using map() and a lambda function.
list4=["Good","Night","Waris","Have","a","Sweet","Dream"]
Concate=list(map(lambda x:x+' ',list4))
print("The value after concate is=",Concate)

# Question
# **Convert a list of temperatures from Celsius to Fahrenheit using map() and a conversion formula
TempOfCelcius=[12,13,14,15,16,17,19]
Fahrenheit=list(map(lambda x: (x*9/5)+32,TempOfCelcius))
print("The list of temp in TempToFarehnhit is=",Fahrenheit)