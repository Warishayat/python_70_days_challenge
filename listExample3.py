
# Create a list of squares for numbers from 1 to 5.

l1=[n**2 for n in range(1,5)]
print(l1)


# Create a list of the first letter of each word in a sentence
fruit=["mango", "pineapple", "avacado","watermelon","Dragon","Grapes"]
for i in fruit:
    print(i[0])


# Create a list of even numbers from 1 to 10..
#list comprehension
l=[l for l in range(1,10) if l%2==0]
print(l)


