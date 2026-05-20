def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    return x / y if y != 0 else "Error! Division by zero."

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")