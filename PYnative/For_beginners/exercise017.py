# generate Fibonacci series up to 15 items
# first two numbers
num_1, num_2 = 0, 1

print("Fibonacci sequence: ")

# run loop 15 items
for i in range(15):
    # print next number of a series
    print(num_1, end=" ")
    # add last two numbers to get next number
    res = num_1 + num_2
    # update values
    num_1 = num_2
    num_2 = res
    