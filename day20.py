#tuple method. how to maniulate into tuple.

l=(1,2,3,4,5,6,99,7,8,9,10)
l1=(11,22,33,44,55,66,77,77,88,99,110)
temp=list(l)    #here we convert tuple to list.
print(type(temp))
temp.append(16)  #make changes
temp.insert(1,22)  #insert values 22 at index 1.
# temp.sort()
print(temp)
l=tuple(temp)  #again convert list to tuple
print(type(l),l)
#if we want to chnage something first we will convert tuple to list than make changes then again convert that kist into tuple.
k=l+l1     #here we concate the two couple.q
print(k)

#method
m=k.count(77)
print(m)
#indexing
m=l.index(1)
print(m)
m=l.index(99,5,10)
print(m,end=" ")