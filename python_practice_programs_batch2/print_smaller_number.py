print("This program will print the smaller number.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("\nThe numbers are equal.")
else:
    print("\nThe smaller number is ", min(num1, num2))