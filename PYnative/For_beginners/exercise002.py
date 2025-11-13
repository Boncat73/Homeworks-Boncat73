# Write Python code to iterate through the first 10 numbers and, in each iteration,
# print the sum of the current and previous number.

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + i
    print("Current number", i, "Previous number ", previous_num, " Sum: ", x_sum)
    previous_num = i
