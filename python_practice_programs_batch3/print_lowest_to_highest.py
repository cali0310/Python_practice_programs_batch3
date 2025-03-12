print("This program will continue asking until the user input is invalid.\n It will display the number from lowest to highest.\n")

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Numbers sorted from lowest to highest value:", numbers)