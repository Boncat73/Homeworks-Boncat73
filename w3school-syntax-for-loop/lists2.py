# Task 1 start
# Creat first and second lists
team_a = ["Петро", "Ірина", "Ганна", "Олег"]
team_b = ["Марія", "Василь", "Олексій"]

# copy first list and add him to second list
all_people = team_a.copy()
all_people = team_a + team_b

# remote first person
remote_pacient = all_people.pop()

# to sort new list
all_people.sort()

# print result
print(f"Remote pacient: {remote_pacient}")
print(f"new_team (sort): {all_people}")
print(type(all_people))
# Task 1 end

# Task 2 start
# Analysis of results
results = [4, 5, 3, 5, 4, 2, 5, 4]

#results = len(results)

results_5 = results.count(5)

results_4 = results.count(4)

results_3 = results.count(3)

results_2 = results.count(2)

# remove result 2
results.remove(2)

print(len(results))
print(f"Results: {results}.")
print(f"Result 5: {results_5}")
print(f"Result 4: {results_4}.")
print(f"Result 3: {results_3}.")
print(f"Result 2: {results_2}.")
print(type(results))
# Task 2 end

# Task 3 start
# List constructor for make a list
thislist = list(("apple", "bananba", "cherry", "kiwi", "apricot"))
print(thislist)
print(type(thislist))
print(thislist[2])
print(len(thislist))
print(thislist[4])
print(thislist[:3])
print(thislist[2:])
print(thislist[1::3])
print(thislist[-1])
print(thislist[-3:-1])
# Task 3 end

# Task 4 start
thislist_1 = ["apple", "banana", "apricot", "kiwi"]
if "apple" in thislist_1:
    print("Yes, 'apple' is in the fruits list")
# Task 4 end