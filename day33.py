# #this is day 33 of python and todday i will solve the exercise 
# #write a python program to translate the secrate message into code language
# #some of the rules are as fallow:

# #if the word containing 3 letter remove first letter and append that at the end of the word
# #now append 3 random character at the starting and end of that word.
# #if the length of the word is less then 2 char simple reverse the string

# #ask user to keep remind the secrat number to decode the
# #decoding
# #if the word contain less then 3 word then reverse it.
# # else:
# # remove 3 random character from start and end and append the last alphabat at the very ist position

num=input("Enter the secrat message: ")
length=len(num)
print("The length of the Messafe is:",length)
randA='hjk'
randB='kll'
if len(num) >= 3:
    num=num[1::]+num[0]
    num=randA+num[0::]
    num=num[0::]+randB
    print("Your message is on the way to going encode:")
    print("Message Encode:",num)
else:
    code=" ".join(reversed(num))
    print("Your message is on the way to going encode:")
    print("Message Encode:",code)
take_input=input("Do you want to decode the message (y/n):")
if take_input.lower()=='y':
    import random
    getResult=random.randint(1,10)
    print(getResult)
    print("Keep remaind computer genrating number:")
    typ=int(input("What was the number:"))
    if typ==getResult:
        if len(num)>=3:
            num=num[3:length+3:]
            num=num[-1]+num[0:length-1:]
            print("Your message is on the way to going decode:")
            print("Message Succesfully decode:",num)
            
        else:
            num=num[::-1]
            num="".join(reversed(num))
            print("Your message is on the way to going decode:")
            print("Message Succesfully decode",num)
elif take_input.lower() !='n':
    print("You Enter some invalid Number")
else:
    pass
    

