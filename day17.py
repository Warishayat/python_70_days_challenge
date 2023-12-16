# list
#order will be stay maintain.values eprated by comas and open&close by brackets.
#list index work like strings.
l=[3,5,6,6,7,8,9]
print(len(l))
print(len(l))
print(7 in l)               
print(l[-3])                #taotal length - slice == answer
#if i want to append any new number in list
l.append(8)
print("The new value 8 is append in list:",l)
#negative slicing
print("The new asnwer is",l[1:-4])
#jum index
print(l[0:5:2])


#jump index same thing will apply for string(memership operator)
if "ar" in "waris":
    print("True")

#list comprehension
#we genrate the list on the spot:
lst=[ i for i in range(10)]
print(lst)


#now i will jus print the odd number of the list
lst=[ i for i in range(10) if i% 2 != 0]
print(lst)