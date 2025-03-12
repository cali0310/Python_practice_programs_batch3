print("This program will print the numbers between two numbers.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    num1, num2 = num2, num1  # Ensure correct order
for i in range(num1 + 1, num2):
    print(i, end=' ')