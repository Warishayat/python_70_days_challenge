# is vs == in python
#is operator compare identity
#== compare values  
a=4
b='4'
print(a is b) #it gave us false becuase a store diffrent memory location then b
print(a==b) #it gave us false because b("4") is string #values

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]

print(list1  is list2) #false because diffrent memory location
print(list1  == list2) #true because == ompare values

#but if we have constant value then we get both true;
a="hellow"
b="hellow"

print(a is b)
print(a==b)
