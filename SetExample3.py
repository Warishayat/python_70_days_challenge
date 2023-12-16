# Given two lists:
# Write a function that returns a set containing the common 
# elements between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


def commonelement(list1,list2):
    list=set(list1)
    list2=set(list2)

    set3=list.intersection(list2)
    return set3

final_result=commonelement(list1,list2)
print("The commmon elemensts are:",final_result)
print("The type of the set are ",type(final_result))



# Remove Common Elements:
# Given three sets:

# Write a function to remove common elements from the sets and return the updated sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 6, 7, 8, 9}

def rmCommonElemnt(set1,set2,set3):
    final=set2.intersection(set1)
    print(final)
    final_result=set3.intersection(final)
    return final_result
getResult=rmCommonElemnt(set1,set2,set3)

print("The common value in all thee sets are:",getResult)