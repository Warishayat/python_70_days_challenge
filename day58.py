# #walrus operators
# # Assign values to variables as partas largest  expression

# foods=[]
# while (food:= input ("What food do you like:?")) != "quit":
#     foods.append(food)

# #question
# list=[1,2,3,4,5]
# while(number:=len(list))>0:
#     print(list.pop())

# #EXAMPLE
# #     print(a:=100-1)
# # data=[12,13,14,15,16,17]

# # n=len(data)
# # i=0
# # while (i:=i+1) <(n := len(data)):
# #     print(data[i])
    
# # l=[12,13,14,15,16,17]

# # while i:=(len(l)) > 1:
# #     print(l.pop())

# # read number from user and print its positive r negative
# (number:= input("Enter the number")) 


# #(:=)
# name="waris"
# print(name)
# # print(name="waris")

# # print(name:=input("Enter the name"))

# # print(num:=int(input("Enter the number")))
# # print(num2:=int(input("ENTER THE NUMBER 2")))

# #tell which number is greater a or b
# if (a:=int(input("nUMBER 1:")))>(b:=int(input("nUMBER 2:"))):
#     print(a)
# else:
#     print(b)

# print(res:=("A is bigger") if (a:=int(input("Enter the number1"))) > (b:=int(input("Enter the number2"))) else "B is gretaer")

#find the number is positive or nagitive 


# print(result:="Number is positive " if (a:=int(input("Enter the number"))) > 0 else "negative")



#find themaximum number from the list using walrus operator
l=[12,5,6,8,9,12,9]
number=0
for i in l:
    for j in range(1,len(l),1):
        if  i==j:
            print(i)
        else:
            pass
    


        