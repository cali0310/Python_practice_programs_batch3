print("This program will display all numbers. For numbers with duplicate, display only the first entry.\n")

numbers = []
duplicate = set()
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    if num not in duplicate:
        numbers.append(num)

    duplicate.add(num)

print("First occurrences of numbers displayed:", numbers)