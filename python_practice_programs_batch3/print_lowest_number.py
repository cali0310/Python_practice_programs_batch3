numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

    except ValueError:
        break

if numbers:
    lowest = numbers[0]
    
    for num in numbers:
        if num < lowest:
            lowest = num
    
    print("Lowest number:", lowest)
else:
    print("No numbers entered")