print("This program will ask user to input a number until the user input is invalid.\n"
"It will display 'Unique'  when the number does not have duplicate.\nIt will display 'Duplicate' when the number have duplicate.\n")
numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
        
        numbers.append(num)

    except ValueError:
        break
