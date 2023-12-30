
# 1:**Find the product of all elements in a list using reduce() and a lambda function.
from functools import reduce
l=[1,2,3,4,5]

product=reduce(lambda x,y:x*y,l)
print("The new result is:",product)

# 2:**Concatenate all strings in a list using reduce() and a lambda function.
from functools import reduce
Cstr=["Hellow","world","Waris","Hayat","Abbasi"]
final_result=reduce(lambda x,y:x+y,Cstr)
print(final_result)

#3 **Find the maximum element in a list using reduce() and the max function.
from functools import reduce
MaxList=[23,56,88,5,7,7,22,44,66,1222,22,23,45,66,999,44]
def maxelement(x,y):
    if x>y:
        return x
    return y

Checkelement=reduce(maxelement,MaxList)
print("New List here:",Checkelement)

#4: **Join a list of words into a sentence using reduce() and a lambda function.

l=["hey","Good","Morning","waris","Do","the","code"]

join_sentense=reduce(lambda x,y:x+' '+y,l)
print("The sentence is here:",join_sentense)

