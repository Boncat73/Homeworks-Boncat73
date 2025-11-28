# Python - loop lists
# Task 1 start
# you can loop through the list items by using for loop
list1 = ["apple", "banana", "apricot"]
for x in list1:
    print(x)
# Task 1 end

# Task 2 start
# Use the range() and len() functions to create a suitable iterable
list2 = ["chair", "kitchen", "bathroom"]
for i in range(len(list2)):
    print(list2[i])
# Task 2 end

# Task 3 start
# Using a while loop
list3 = ["pen", 24, "True", 21.15, "book"]
i = 0
while i < len(list3):
    print(list3[i])
    i = i + 1

# shotest syntax
list4 = ["pencil", 45, "False", 63.58]
[print(x) for x in list4]
# Task 3 end



 