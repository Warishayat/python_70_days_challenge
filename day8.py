# Day 8/70 challenge and i will cover the multiple condition using logical operator like AND or "or" OERATOR.
#Logical operator help us to combining the elemnt of two elements.

#Suppose there's a girls name wit riya her english marks and science marks greater then 80 then she will get the grade a. or she get 80 in a single subject then she will get the Grade B>

english_marks=int(input("Enter your English Marks:- "))
science_marks=int(input("Enter your English Marks:- "))

#both statment shoukd be true:
if english_marks>=80 and science_marks>=80:
    print("Congrats Riya you get the grade (A))")
#if either of marks more then 80:
elif english_marks>=80 or science_marks>=80:
    print("Congrats Riya you get the grade (B))")
#if non of marls are more then 80:
else:
    print("Congrats Riya you get the grade (C))")