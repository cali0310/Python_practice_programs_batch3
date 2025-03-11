print("This program will print the numbers from 0 to 100 except numbers ending in 0.")

i = 0

while i <= 100:
    if i % 10 != 0:
        print(i, end=' ')
    
    i += 1