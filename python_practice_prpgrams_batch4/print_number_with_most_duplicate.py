print("This program will ask the user to input a number until the user input is invalid and will display the number with the most number of duplicate.\n")
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break  

if num_list:
    most_common = max(set(num_list), key=num_list.count)
    print("Number with most duplicates:", most_common)
else:
    print("No valid numbers entered.")