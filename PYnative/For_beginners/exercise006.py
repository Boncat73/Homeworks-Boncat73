# Display numbers divisible by 5

# create the list
num_list = [10, 20, 33, 46, 55, 78, 92, 25, 105, 75]
print("Given list:", num_list) # print the list
print("Divisible by 5:")       # print message for future results

# create loop to check list elements
for num in num_list:
    if num % 5 == 0: # checking if a list element can be divided by 5 without a remainder
        print(num)   # print result
