print("This program will ask the user to input a number until the user input is invalid and will display the highest number.\n")
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break  

if num_list:
    print("Highest number:", max(num_list))
else:
    print("No valid numbers entered.")