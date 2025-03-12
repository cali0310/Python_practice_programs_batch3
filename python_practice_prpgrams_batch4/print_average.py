print("This program will ask the user to input a number until the user input is invalid and will display the average.\n")
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break  

if num_list:
    average = sum(num_list) / len(num_list)
    print("Average of entered numbers:", average)
else:
    print("No valid numbers entered.")