import time as t

m=t.ctime()
print(m)
if m>='9' and m<'15':
    print("Good mornning")

elif m>='15' and m <= "22":
    print("Good afternoon")
else:
    print("Good night have a sweet dream")