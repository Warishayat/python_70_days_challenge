# Write a program that iterates through numbers from 1 to 20 using a loop.
# If the number is divisible by 4, skip that iteration using continue.
# If the number is greater than 15, break out of the loop.


num=int(input("Enter a number for loop:"))

for i in range(1,num+1,1):
    if i%4 == 0:
        continue
    elif i>=15:
        break
    else:
        print(i)