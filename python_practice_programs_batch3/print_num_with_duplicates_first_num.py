print("This program will display all numbers. For numbers with duplicate, display only the first entry.\n")

numbers = []
duplicates = set()
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))