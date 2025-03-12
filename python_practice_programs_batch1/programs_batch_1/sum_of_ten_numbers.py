print("This program will print the sum of ten numbers.\n")
numbers = []  
for i in range(10):  
    num = float(input(f"Enter number {i+1}: ")  )
    numbers.append(num)  
print("\nThe sum of the numbers is", sum(numbers))