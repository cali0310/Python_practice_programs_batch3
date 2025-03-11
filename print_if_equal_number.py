#input num1
#input num2
#if num1==num2
    #print the numbers are equal
#else
    #print the numbers are not equal

print("This program will ask you to enter two numbers and print 'EQUAL' if both numbers are the same.\n")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1==number2:
    print("\nThe numbers are EQUAL.")
else:
    print("\nThe numbers are NOT EQUAL.")