#tosday we will cover the basic of the enumerates function
#if we want to point out the index directly without enumerates:
lest=[100,89,33,444,55,67]
index=0
for i in lest:
    print(i)
    if (index == 3):
        print("zeeshan marks are:",i)
    index+=1


#now we will do the same thing with enumerates:
lst=[100,89,33,444,55,67]
for index,marks in enumerate(lst):
    print(f"we have marks {marks} at index: {index}")


#same thing can be happen with string
strng ="apple,mango"
for index,fruit in enumerate(strng):
    print(index,fruit)

#practise example


# Question: Create an enumeration named Days with the 
# days of the week (Monday through Sunday). Then, write a 
# function called print_day that takes a day parameter of 
# type Days and prints "It's [day]!" where [day] is the actual day.
# Finally, call the function with a specific day.

days=['sunday','monday','tuesday','wednesday','Thurusday','Friday','Saturday']

for index,days in enumerate(days,start=1):
    print(index, ":" ,days)
    