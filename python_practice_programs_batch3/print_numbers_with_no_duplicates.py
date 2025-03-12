print("This program will print the numbers without duplicates.\n")

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

unique_numbers = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count == 1:
        unique_numbers.append(numbers[i])

print("\nNumbers without duplicates:", unique_numbers)