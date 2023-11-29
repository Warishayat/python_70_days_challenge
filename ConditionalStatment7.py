#Ques: Take input percentage of the student and print the grading according to therir marks>
#81-100-->A Grade
#61-80-->B Grade
#41-60--> C Average
#<=40 fail
# its the part of 

marks=float(input("Enter your Percentage:-"))

if marks>=81:
    print("Suceessfully you acheive the GRADE A :-) ")
elif marks>=61:
    print("Wao you acheive the GRADE B :-) ")
elif marks>=40:
    print("you acheive the GRADE C :-) ")
else:
    print("you acheive the GRADE F or (FAIL):-) ")
