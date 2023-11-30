# You are tasked with creating a registration system for a conference. Write a Python script to determine if a person is eligible for registration based on the following conditions:

# If the age is below 18, they are not eligible for registration.
# If the age is between 18 and 25 (inclusive) and they are a student, they are eligible for registration.
# If the age is between 26 and 40 (inclusive) and they have a discount code, they are eligible for registration.
# If the age is above 40, they are eligible for registration regardless of other conditions.
# Take user input for age, student status, and discount code availability. Determine and display whether the person is eligible for registration based on the given conditions.

print("********Registration system for the conference**********")
age=int(input("Enter your age:"))
Student=input("Are you a student type only (y/n): ")
if Student.lower()=='y':
    is_student=True
else:
    is_student=False
Discountcode=input("Do you have Discount Code type only (y/n): ")
if Discountcode.lower()=='y':
    is_discountCOde=True
else:
    is_discountCOde=False
 

if (age<18):
    print("Sorry! you are not eligible for the registration:")
elif (age >= 18 and age < 25) and (is_student):
    print("Congrats You are eligible for Registration:")
elif (age >=25 and age < 40) and (is_discountCOde):
    print("Congrats You are eligible for Registration:")
elif (age>=40):
    print("You are eligible for the Registration:")
else:
    print("You are not eligible for the Registration:")