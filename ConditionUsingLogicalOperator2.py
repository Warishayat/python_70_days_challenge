# Write a Python script that determines the ticket price based on the following conditions:

# If the age is 12 or below, the ticket price is $5.
# If the age is between 13 and 18 (inclusive) and the person is a student, the ticket price is $8.
# If the age is between 13 and 18 (inclusive) and the person is not a student, the ticket price is $10.
# If the age is 19 or above, the ticket price is $12.
# Take user input for age and whether they are a student, then calculate and display the ticket price based on the given conditions.
age=int(input("Enter Yor age: "))
student=input("Are you a Student:(y/n)")
if student.lower()=='y':
    is_student=True
else:
    is_student=False

if age<=13:
    print("The ticket price is $5 only.")
elif (age >13 and age <= 18 ) and (is_student):
    print("The ticket price is $8 only.")
elif (age >13 and age <= 18 ) and (is_student!=True):
    print("The ticket price is $10 only.")
else:
    print("The tickey price is only $12.")
