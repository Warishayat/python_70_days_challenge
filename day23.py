#Today i will cover the basic of sets
#Set is the well defined object. repetation is not allowed in the set.


st={1,2,3,4,5}
print(type(st))


# #how to print empty set.
st2=set()
print(type(st2))

# #how to  make sets beucause set never allow the repetation values
data={
    42, "apple", 3.14, "banana", True, (1, 2, 3), "orange", 7, "kiwi", 2.718,
    False, "grape", (4, 5, 6), 10, "watermelon", 99.9, "strawberry", (7, 8, 9),
    "pineapple", "elephant", 55, 8.8, "tomato", (10, 11, 12), "pear", 6, "mango",
    "carrot", 77.7, "peach", (13, 14, 15), "cherry", "lion", 31, 4.4, "blueberry",
    (16, 17, 18), "plum", "tiger", "cucumber", 22, 1.1, "raspberry", (19, 20, 21),
    "melon", "panda", 88, "broccoli", "avocado", 2.22, "blackberry", (22, 23, 24),
    "pepper", "elephant", 11, "lime", "kiwi", (25, 26, 27), "apple", "orange", 16.5,
    "grape", "lemon", 3, 99.99, "fig", "elephant", (28, 29, 30), "strawberry", "cherry",
    7, "peach", "pear", 5.55, "watermelon", "blueberry", (31, 32, 33), "plum", "panda",
    66, "carrot", "tomato", 9.8, "melon", (34, 35, 36), "mango", "lion", "cucumber",
    "avocado", "broccoli", 44, 6.66, "raspberry", (37, 38, 39), "lime", "banana",
    "tiger", "pepper"
}

data2 ={
    42, "apple", 3.14, "banana", True, (1, 2, 3), "orange", 7, "kiwi", 2.718,
    False, "grape", (4, 5, 6), 10, "watermelon", 99.9, "strawberry", (7, 8, 9),
    "pineapple", "elephant", 55, 8.8, "tomato", (10, 11, 12), "pear", 6, "mango",
    "carrot", 77.7, "peach", (13, 14, 15), "cherry", "lion", 31, 4.4, "blueberry",
    (16, 17, 18), "plum", "tiger", "cucumber", 22, 1.1, "raspberry", (19, 20, 21),
    "melon", "panda", 88, "broccoli", "avocado", 2.22, "blackberry", (22, 23, 24),
    "pepper", "elephant", 11, "lime", "kiwi", (25, 26, 27), "apple", "orange", 16.5,
    "grape", "lemon", 3, 99.99, "fig", "elephant", (28, 29, 30), "strawberry", "cherry",
    7, "peach", "pear", 5.55, "watermelon", "blueberry", (31, 32, 33), "plum", "panda",
    66, "carrot", "tomato", 9.8, "melon", (34, 35, 36), "mango", "lion", "cucumber",
    "avocado", "broccoli", 44, 6.66, "raspberry", (37, 38, 39), "lime", "banana",
    "tiger", "pepper"
}
print(data.intersection(data2))

# #if we want to concate the two set.
data3=data.union(data2)

# #how to apply loop on tha given data:
for i in data3:
    print(data3,end="")
print()


# #find the same value from two diffrent sets.

data4={1,2,5,4}
data5={7,22}
# #add some value in data4.
data5.add(199)
print(data5)

#if we want to update some set
# data4.update(data5)
# print(data4)
# #same values in the set.
c=data4.intersection(data5)
print(c)

# to ceck the diffrence between the data set.
data6=data4.difference(data5)
print("The diffrence is",data6)

#how to update the values from set.
data4={1,2,5,4}
data5={7,22}
data4.discard(1)
count=0
odd=0
print(data4)
for i in data4:
    
    if i% 2==0:
        count+=1
    else:
        odd+=1
print("The value of data set are",i,"Even values are:",count,"Odd values are:",odd)
# #to do some thing discard from the set.
data5.discard(22)
print(data5)

# #to pop something from the set that will be delet random
data4.pop()
print(data4)

# #add some value in data4.
data5.add(199)
print(data5)

# # to check disjoint that mean intersection should be empty():
print(data5.isdisjoint(data4))

# #to check subset mean data5 is the subset of set of data4:
print(data5.issubset(data4))

# #to check superset mean data4 is the powerset of set of data5:
print(data4.issuperset(data5))

# #to remove som ething from the set.
data4.remove(5)
print(data4)

# #to clear the data set
data4.clear()
print(data4)

# #to check some value through membership operator that is presemt in the data or not:
data4={1,2,5,4}
if 2 in data4:
    print("2 is present:")
else:
    print("Not present")