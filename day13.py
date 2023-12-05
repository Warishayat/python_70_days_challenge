#Question solve the pattern question ?

n=int(input("Enter the rows: "))

for  _ in range(n):
    print("*"*5)

for i in range(1,9):
    for j in range(1,9):
        print(j ,end= " ")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
#next question
for i in range(1,8):
    for n in range(1,i):
        print(n,end =" ")
    print()

#solve the new question

n=int(input("Enter the N:"))

for i in range(1,n):   # fo rowse
    print(" " * (n-i), end=" ")  #for space
    for n in range (1,2*i):
            print(n,end=" ")
    print()



