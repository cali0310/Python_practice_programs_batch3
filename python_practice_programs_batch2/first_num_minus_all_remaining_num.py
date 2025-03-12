print("This program will print the result when the first number minus all remaining numbers.")

num = []

for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    num.append(number)

remaining = sum(num[1:])
print("Sum of the numbers except the first number is", remaining)

result = num[0] - remaining
print("\nThe result is", result)