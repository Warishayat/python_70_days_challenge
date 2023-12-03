#And operator ==>logial operator
a=10
b=20
c=10
if a==c and b==c:
    print("All are true:")
else:
    print("All are not true:")

#Or operator
a=10
b=20
c=10
if a==c or b==c:
    print("Atleast one is true:")
else:
    print("Ateast no one is true:")

#Not operator
a=10
b=20
c=10
if not a==c:
    print("Atleast one is true:")
else:
    print("Ateast no one is true:")


#identity operator  (is) operator if all the variable are same.
c=5
y=6
print("x is y", c is y)
print("x is y", c is not y)

#membership operator  (in operator) return true if the value is present is sequence and vice versa for not in.
list=[1,2,3,4]
print(1 in list)    ##it should be true because 1 exist in list
print(5 in list)    #it should be false because 5 never exist in list

#bitwise opreator like 0 and 1 is bit and its called binary number system.

a=10
b=23
print("A and B is:",a & b)
print("A not B is:",a | b)
print("A xor B is:",a ^ b)

#opreator precedence if there are many operator which will precede first we will follow 
#BODMAS Rule (Bracket open than division,than multipication,than addition and than subtraction).
