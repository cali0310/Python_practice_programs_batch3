print("This program will print all the numbers starting from 0 to 100 except numbers ending in zero or ending in five.\n")

i = 0
while i <= 100:  
    if i % 10 != 0 and i % 10 != 5:  
        print(i, end=' ')  
    i += 1