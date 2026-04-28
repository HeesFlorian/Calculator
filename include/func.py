import math

# Function definitions for the Calculator class

def add(a, b):
    "Return the sum of a and b."
    return a + b
def subtract(a, b):
    "Return the difference of a and b."
    return a - b
def multiply(a, b):
    "Return the product of a and b."
    return a * b
def divide(a, b):
    "Return the quotient of a and b. Raises ValueError if b is zero."
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    "Return a raised to the power of b."
    return a ** b
def sqrt(a):
    "Return the square root of a. Raises ValueError if a is negative."
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5
def factorial(n):
    "Return the factorial of n. Raises ValueError if n is negative."
    if n < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def log(a, base=10):
    "Return the logarithm of a to the given base. Raises ValueError if a is non-positive or base is less than or equal to 1."
    if a <= 0:
        raise ValueError("Cannot take the logarithm of a non-positive number.")
    if base <= 1:
        raise ValueError("Base must be greater than 1.")
    return math.log(a, base)
def sin(angle):
    "Return the sine of the given angle in degrees."
    return math.sin(math.radians(angle))
def cos(angle):
    "Return the cosine of the given angle in degrees."
    return math.cos(math.radians(angle))
def tan(angle):
    "Return the tangent of the given angle in degrees. Raises ValueError if the angle is 90 degrees or 270 degrees."
    if angle % 180 == 90:
        raise ValueError("Tangent is undefined for angles of 90 degrees and 270 degrees.")
    return math.tan(math.radians(angle))
