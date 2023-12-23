import random as rd
#it wil print a random number when i will print rd
print(rd)

#it will choose a random value from list
list1=["snake","fire","Gun"]
result=rd.choice(list1)
print(result)

#now it will choose a single value from list2 string
list2="warisisdoingprogramming"
result2=rd.choice(list2)
print(result2)

#now ue randint function/method
#it will print random integer betwnn 10and 20
print(rd.randint(10,20))


#now i will use sample method
list3=(1,2,3,4,5,6,7,8,9)
#it will gave us sample value in print
result=rd.sample(list3,5)
print(result)


#now i will shuffle a tuple
list3=[1,2,3,4,5,6,7,8,9]
print("List before shuffle:",list3)
rd.shuffle(list3)
print("List after shuffle:",list3)