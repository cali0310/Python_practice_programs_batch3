print("This program will print the remainder of first number divided by the second number.\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
while num2==0:
    print("Division by O will result to undefined. Try again.")
    num2 = float(input("Enter the second number: "))

print("\nThe remainder of the two numbers is ", num1%num2)