# Task 1 start
# Change item value
thislist = ["apple", "banana", "cherry", "kiwi", "apricot"]
thislist[1] = "apricot"
print(thislist)
# Task 1 end

# Task 2 start
# Change a range of item values
thislist_things = ["pen", "pencil", "laptop", "table", "book"]
thislist_things[1::3] = ["picture", "door"]
print(thislist_things)
# Task 2 end

# Task 3 start
# Insert items
thislist_1 = ["sky", "morning", 24, "True", thislist_things, "fox"]
thislist_1.insert(2, "armchair")
print(thislist_1)
# Task 3 end

# Task 4 start
# Append items
thilist_2 = [thislist_1, thislist, thislist_things, 84, "False"]
thilist_2.append("orange")
print(thilist_2)
# Task 4 end

# Task 5 start
# Extend list
fruits = ["apple", "apricot"]
fruits_tropic = ["banana", "kiwi", "orange"]
fruits.extend(fruits_tropic)
print(fruits)
# Task 5 end

# Task 6 start
# Remove specified item
things = ["book", "pencil", "table"]
things.remove("pencil")
print(things)
# Task 6 end

# Task 7 start
# Remove specified index
things2 = ["books", "pencils", "tables"]
things2.pop(1)
print(things2)
# Task 7 end

# Task 8 start
# The del keyword also removes the specified index
things3 = ["chair1", "chair2", "chair3"]
del things3[1]
print(things3)
# Task 8 end

# Task 9 start
# The del keyword can also delete the list completely
things_4 = ["skarf", "hat", "dress", "laptop"]
del things_4
# Task 9 end

# Task 10 start
# Clear the list
color_list = ["red", "blue", "white", "black"]
color_list.clear()
print(color_list)
# Task 10 end