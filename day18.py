# python method today i will cover the diffrent diffrent method of list
l1=[51,52,53,54,55,56]
l=[177,199,2,3,333,2,4,5,6]
l.sort(reverse=True)
l.sort()
l.extend(l1)
m=l.count(2)
l1.remove(51)
l1=l.copy()
l1[0]=9
print(l)
print(l1)
#concatinate
k=l+l1
print(k)
print(len(l1))
print(l1.index(2))