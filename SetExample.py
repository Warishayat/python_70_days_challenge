#set basic exampl
#combine all the element of both set
a={1,1,2,2,2,2,2}
b={4,3,2,1,1,1}
print(a.union(b))
#now get the same element from the set
print(a.intersection(b))

# repetation is not allowed in set
st={1,1,2,3,4,5,5,6,7,8}
print("This will never print:",st)

#difrence between the set
print("The diffrence between two set are",a.difference(b))
#now we will check a is the subset of b or not
a={1,2,3,4}
b={3,4}
print(b.issubset(a))
print("A is the power set of B:",a.issuperset(b))

#how to clear a set
print("The value of set B is:",b.clear())

#now i want to remove a single element from the set
Nom={1,2,3,4,5,6}
Nom.remove(4)
print(Nom)

main_set = {1, 2, 3}
print("2,3 is subset") if 2 and 3 in main_set else print("2 is subset") if 2 in main_set else print("3 is subset:")


