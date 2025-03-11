print("This program will print the number of odd numbers from the entered values.\n")

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

odds = 0
for num in numbers:
    if num % 2 != 0:
        odds += 1

print("The number of odd numbers entered is:", odds)