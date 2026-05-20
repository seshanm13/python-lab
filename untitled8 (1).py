def calculate_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input("Enter a number to find factorial: "))
print(f"Factorial of {num} is {calculate_factorial(num)}")