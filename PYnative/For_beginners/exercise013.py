# Write a code to generates a complete multiplication 
# table for numbers 1 through 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

print()    

for i in range(1, 11):
    # printing string, if i even
    if i % 2 == 0:
        for j in range(1, 11):
            print(i * j, end=" ")
        
        print()

print() 

for i in range(1, 11):
    # printing string, if i not even
    for j in range(1, 11):
        result = i * j
        if result % 2 != 0:
            print(result, end=" ")
        else:
            print(end=" ")
    print()
