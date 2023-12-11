# Access the first and last elements of a list.
fruit=["mango", "pineapple", "avacado","watermelon","Dragon","Grapes"]
print(fruit[1])
print(fruit[5])


# Access the second and third elements using slicing.
fruit=["mango", "pineapple", "avacado","watermelon","Dragon","Grapes"]

print(fruit[2:4])

# Modify an element in the middle of a list.

fruit=["mango", "pineapple", "avacado","watermelon","Dragon","Grapes"]
fruit.insert(1,"banana")
print(fruit) 
fruit.append("Cucumber")
print(fruit)
fruit.pop()
print(fruit)
fruit.remove("avacado")
print(fruit)
fruit.reverse()
print(fruit)
sorted(fruit)
print(fruit)
fruit.sort(reverse=True)
print(fruit)
