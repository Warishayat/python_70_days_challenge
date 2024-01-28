#Day 12/70 i will cover the loop>
#we have two type of loop for loop and while loop.
# FOR is a pre built key Then we initialized a variable then in range mean what will be range of n start to end 
#  e.g = for i in range( 1(start),10(end),1(move forward by 1)) it will work 1 to 9.
#FOR loop give the idea of number of iteration.

for _ in range(1,11):
   print("i dont have n variable right now i jus want to print loop.")


#Q print element of a list using loop?
#list is the sequence of the element e.g=[1,2,3,4,5]
#list =[10,20,30,40,50,60]

list =["apple","banana","mango","avacado"]

for i in list:
    print(i)


#while lOOP 
#it runs untill the condtion is true.

n=0
while(n<10):
    print(n)
    n=n+1

#Question : print the even number between initialized and end point?
initial=2
while (initial<=100):
    if initial % 2 == 0:
        print("Number is even ",initial)
    else:
        pass
    initial=initial+2

