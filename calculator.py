import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def log(x):
    if x <= 0:
        return "Cannot calculate log of non-positive number"
    return math.log(x)

# Example usage
num1 = 10
num2 = 5

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Logarithm:", log(num1))