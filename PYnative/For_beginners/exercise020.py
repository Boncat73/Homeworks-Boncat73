# print Reverse Number Pattern

def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i + 1):
            print(i, end = " ")
        print() # move to next line after each row

# print the pattern for with 5, 7 and 10 rows
print_pattern(5)
print_pattern(7)
print_pattern(10)


