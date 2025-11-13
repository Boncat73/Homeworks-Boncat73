# Check if the first and last numbers of a list are the same.

# create a function that takes one argument - a list
def first_last_same(numberList):
    print("Given list:", numberList) # print the list

    first_num = numberList[0] # extract the first element of the list
    last_num = numberList[-1] # extract the last element of the list

    # check whether the first element of the list is equal to the second
    if first_num == last_num:
        return True
    else:
        return False

# create lists and call the function, printing the result
numbers_x = [10, 20, 30, 40, 10]
print("Result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Resilt is", first_last_same(numbers_y))
