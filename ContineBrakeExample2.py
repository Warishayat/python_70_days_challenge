# Implement a password checker using a loop.
# Ask the user to enter a password, and 
# keep asking until they enter the correct password "password123".
# Use break to exit the loop once the correct password is entered.

password=input("Set the password: ")

while True:

    againpass=input("Again enter the password: ")

    if againpass==password:
        print("Now you password fullfill the req.")
        break
    else:
        print("You enter the wrong password! try again.")
