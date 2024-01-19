#generator  are use for memor efficency it genrate the value on the fly whenever we need the value
#it does not make the list in a whole loop i genrate the only valuehich is needed.
def my_genrator():
    for i in range(5):
        yield i 
result=my_genrator()
print(next(result))
print(next(result))
print(next(result))
print(list(result))


#Write a generator function called square_generator that generates the 
#squares of numbers from 1 to a given limit (n)
def square_generator(n):
    for i in range(n):
      yield i**2
x=square_generator(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Create a generator function called even_numbers that generates even numbers up to a
#  given limit (n).

def even_numbers(n):
    for i in range(n):
        if i%2==0:
            yield i
        else:
            pass

result=even_numbers(10)
print(list(result))