#python tuple which are unchangeble un mutale its seprated by comas and enclosed by round bracket. ().

tep=(1,2,3,7,5,6,7,8,9,10,12)
print(tep.count(7))
print(type(tep))
print(13 in tep) 
#indexing working same like list here.
print(tep[0])  #we can caught value through index.
print(tep[1])
print(tep[2])
print(tep[3])
print(tep[4])
#length of tuple
print("The total length of tuple is",len(tep))
print(tep[:-5])  #Total length is 11 and 11-5=6 it will print first six value:
print(tep[2:10]) #it start from to 2 and goes upto 10.


# if 6 and 7 and 14 in tep:   #Membership operator.
print("These number are present.")
else:
print("Not present.")
#negative slicing
print(tep[:-7])