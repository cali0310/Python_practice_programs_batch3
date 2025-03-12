print("This program will print the quotient of the two numbers.\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 == 0:
    print("The first number cannot be divided by 0.")
    exit()
else:
    print("\nThe quotient of the two numbers is ", num1/num2)