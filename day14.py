# -----> Day14/70 today i will cover the break and continue statments in deep and  i will \n
# to solve hard and medium level of example of braake and continue statments.


#Continue:

for i in range(1,6):
    if i==3:
         continue                   # when i will be 3 further code will be not execute for that iteration
    else:
        print(i,end =" ") 
print()
name='Waris Hayat'
for i in name:
   if  i=='a':
       continue
   else:
       print(i,end=" ")

########################## (Break_Statment)###########################3

for i in range(1,10,1):
    if i==7:
        break
    else:
        print(i)

list=[10,12,13,14,15,16,17]

for i in list:
    if i==14:
        print("14 found here.")
        break
    else:
        print("Still not found.")


####break with string statments:


name="Coding is Fun"

for i in name:
    if i=="i":              #code will break after "co" because after that is "i".
        print("Found here!") 
        break
    else:
        print("Still not found",i)