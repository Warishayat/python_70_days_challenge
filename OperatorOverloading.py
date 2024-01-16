#Add the two vector by using dunder method and operator overloading
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D (self.x + other.x , self.y + other.y)

# Test your implementation
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
result = v1 + v2
print(f"Result: x={result.x}, y={result.y}")

# Create a class that represents a custom string. Overload the + operator to concatenate two instances of your custom string class.
# python

class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # Define string concatenation here
        return CustomString(self.value + other.value)

# Test your implementation
str1 = CustomString("Hello, ")
str2 = CustomString("world!")
result = str1 + str2
print(result.value)  # Should print "Hello, world!"



# Implement a class representing a complex number. Overload the == operator to compare two complex numbers for equality.
# python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __eq__(self, other):
       return (self.real==other.real , self.imag==other.imag)

# Test your implementation
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(2, 3)
print(result:=(c1 == c2)) 