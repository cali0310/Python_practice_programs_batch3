print("This program will print the number of even numbers from the entered values.\n")

numbers = []

for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

even = 0

for num in numbers:
    if num % 2 == 0:
        even += 1

print("\nThe number of even numbers entered is:", even)