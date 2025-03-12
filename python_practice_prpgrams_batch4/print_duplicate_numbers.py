print("This program will ask user to input 10 numbers and display all numbers that have duplicate.\n")
numbers = []
for i in range(10):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

duplicates = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print("Duplicate numbers are:", duplicates)
