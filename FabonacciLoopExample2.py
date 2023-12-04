#Print the fabonacii series:
l=[0,1]

for i in range(2,10):
    third_num=l[i-1]+ l[i-2]
    l.append(third_num)
print(l)
    