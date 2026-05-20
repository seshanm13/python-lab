def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number to check prime: "))
print(f"Is {num} prime? {is_prime(num)}")