# Write Python code to iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.
# Напишіть код на Python для ітерації по перших 10 числах та, 
# в кожній ітерації, виведення суми поточного та попереднього числа.

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop for 10 numbers
for i in range(1, 11):
    x_sum = previous_num + i
    # print current, previous number and their sum 
    print("Current number", i, "Previous number ", previous_num, " Sum: ", x_sum)
    previous_num = i
