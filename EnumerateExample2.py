# 4: Use enumerate with a custom starting index and print each element.
# Start index: 10
# Expected output:
# 10 one
# 11 two
# 12 three
# 13 four

my_list = ['one', 'two', 'three', 'four']

for key,value in enumerate(my_list,start=10):
    print(f"{key} {value}")



# Given a list and an element, find and print the index of that element using enumerate.
# Expected output: Index of 'banana' is 2
fruits = ['apple', 'orange', 'banana', 'grape']
target_fruit = 'banana'

for key,value in enumerate(fruits):
    if fruits[key]==target_fruit:
        print("Target found at",key)


# Print elements from a list along with their index, but only if the element is a string.
# Expected output:
# 1 apple
# 3 banana
# 5 cherry
mixed_list = [42, 'apple', 3.14, 'banana', True, 'cherry']

for key,value in enumerate(mixed_list):
    if isinstance(value,str):
        print(f"{key} {value}")
      

# Use enumerate with zip to iterate over two lists simultaneously and print their corresponding elements.
# Expected output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 22 years old
        
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

for index,(name,ages) in enumerate(zip(names,ages)):
    print(f"{name} IS {ages} year old")
        
