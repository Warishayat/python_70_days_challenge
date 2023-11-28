number=input("Enter number to check palindrome: ")

left=0
right=len(number)-1
iS_flag=True

while(left<right):
    if number[left] != number[right]:
        iS_flag=False
        break
    left+=1
    right-=1
if iS_flag:
    print("The number is palindrome")
else:
    print("The number is not palindrome")