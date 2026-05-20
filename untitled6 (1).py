def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = int(input("Enter a number: "))
print(f"The number {num} is {check_even_odd(num)}.")