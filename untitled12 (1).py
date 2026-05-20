numbers = []
print("Enter 10 numbers one by one:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

unique_numbers = set(numbers)
print("Unique numbers sequence:", unique_numbers)
print("Total Unique Numbers Count:", len(unique_numbers))