# Given a list, print each element along with its index using enumerate.

# Expected output:
# 0 apple
# 1 banana
# 2 cherry

my_list = ['apple', 'banana', 'cherry']

for index,value in enumerate(my_list):
    print(f"{index} {value}")



# 2:Calculate the sum of indices for all even elements in the list.

# Expected output: 1 + 3 = 4
    
my_numbers = [10, 20, 30, 40, 50]
indices_sum=0
for key, value in enumerate(my_numbers):
    if value%2== 0:
        indices_sum+= key
print("The sum of indices",indices_sum)
        



# 3: Expected output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
my_string = "Python"

for key,value in enumerate(my_string):
    print(f"{key} {value}")
