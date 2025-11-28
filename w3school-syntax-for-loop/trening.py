# Task 1 start
name_user = "Vasyl"
print("Hi,", name_user, ", welcome to the Python!")
# Task 1 end

# Task 2 start
a, b = 3, 8
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# Task 2 end

# Task 3 start
age = 15
if age >= 18:
    print("You are a big person.")
else:
    print("You are a small person.")
# Task 3 end

# Task 4 start
my_fruits = ["apricot", "mango", "banana", "apple"]
print(my_fruits[0])
print(my_fruits[1])
print(my_fruits[2])
print(my_fruits[3])
# Task 4 end

# Task 5 start
for fruit in my_fruits:
    print("I like " + fruit)
# Task 5 end

# Task 6 start
my_fruits = ["apricot", "mango", "banana", "apple"]
for fruit in my_fruits:
    if fruit == "banana":
        print("I like a banana.")
    elif fruit == "apple":
        print("I like an apple.")
    elif fruit == "mango":
        print("I like a mango.")
    elif fruit == "apricot":
        print("i like an apricot!")
    else:
        print("This is ", fruit)
# Task 6 end

# Task 7 start
a = {
    "name1": "user1", "age": 18,
    "name2": "user2", "age": 19,
    "name3": "user3", "age": 20,
    "name4": "user4", "age": 21,
    "name5": "user5", "age": 22,
}
print(a)
print(type(a))
# Task 7 end

# Task 8 start
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers)
print(type(numbers))
# Task 8 end

# Task 9 start
my_things = ["pen", "pencil", "lamp", "laptop", "apple", "Iphone 15"]
print(my_things)
print(my_things[0])
print(my_things[1])
print(my_things[2])
print(my_things[3])
print(my_things[4])
print(my_things[5])
print(type(my_things))
# Task 9 end

# Task 10 start
name = "Vasyl"
print("Hello,", name, ", welcome in Lviv!")

name = "Boris"
if name == "Vasyl":
    print("Hi,", name, "!")
else:
    print("What is your name?")
# Task 10 end

# Task 11 start
dict_book = {
    "num 1": "book 1", "pages": 59,
    "num 2": "book 2", "pages": 116,
    "num 3": "book 3", "pages": 286,
    "num 4": "book 4", "pages": 94,
}
print(dict_book)
print(type(dict_book))
# Task 11 end

# Task 12 start
dict_names = {
    "name 1": "Vasyl", "age": 52,
    "name 2": "George", "age": 20,
    "name 3": "Daniel", "age": 23,
}
print(dict_names)
print(type(dict_names))
# Task 12 end

# Task 13 start
# Create two variables: the first is an integer, the second is a 
# float number as a string. Convert the second number to a float. 
# Add the numbers together, print the result and its type.
num_1 = 5
num_2 = "12.5"

num_2 = float(num_2)
result = num_1 + num_2
print(f"Sum equal: {result}.")
print(f"Type result is {type(result)}.")
# Task 13 end

# Task 14 start
# You have a float variable. Convert her to an int 
# (that is, discard the fractional part). Convert the 
# resulting integer back to str. Print the final value 
# and its type.

num_float = 3.4521
num_float = int(num_float)
num_float = str(num_float)

print(f"Result is: {num_float}")
print(f"Type: {type(num_float)}")
# Task 14 end

# Task 15 start
# String Concatenation. You have an int variable named age. Convert it to str.
# Create a string message using string concatenation that says: 
# "I am [age value] years old." Print the message.

age_person = 52
age_person = str(age_person)
message = "I have " + age_person + " years old."
print(message)
# Task 15 end

# Task 16 start
a = "Hello, world!"
print(a[3])
# Task 16 end

# Task 17 start
for x in "banana":
    print(x)
# Task 17 end

# Task 18 start
str_1 = "Hello, Python!" # length string
print(len(str_1))

str_2 = "The best things in life are free!" # check string
print("free" in str_2)

if "free" in str_2: # use if statement
    print("Yes, 'free' is present.")

print("expensive" not in str_2) # check if NOT

if "expensive" not in str_2:
    print("No, 'expensive' is NOT present.")
# Task 18 end

# Task 19 start
b = "Hello, Python!"
print(b[2:5]) # get the characters form position 2 to position 5 not included
# result: llo

h = "Hello, Python!"
print(h[:5]) # get the characters from the start to position 5 not included
# result: Hello

g = "Hello, Python!"
print(g[2:]) # get the characters from position 2, and all the way to the end
# result: llo, Python!

w = "Hello, Python!"
print(w[-5:-2]) # use negative indexes to start the slice from the end of the string
# result: tho
# Task 19 end

# Task 20 start
# # Modify String
# # methods: upper, lower, title, capitalize, strip, replace, split
c = " Hello, Python! "
print(c.upper())
print(c.lower())
print(c.title())
print(c.capitalize())
print(c.strip())
print(c.replace("H", "D"))
print(c.split())
print(c.split(","))
# Task 20 end

# Task 21 start
# Concatenation String
g = "Hello"
p = "World"
e = g + p
print(g + p)
print(e)
print(g + " " + p)
print(g, p)
print(g + "," + p)
# Task 21 end

# Task 22 start
# # Format String
age = 52
txt = (f"My name is Vasyl, I am {age}.")
print(txt)
# Task 22 end

# Task 23 start
# Placeholders and Modifiers
price_1 = 59
txt_22 = f"The price is {price_1} dollars."
print(txt_22)

txt_33 = f"The price is {price_1:.2f} dollars."
print(txt_33)

txt_44 = f"The price is {20 * 59} dollars."
print(txt_44)
# Task 23 end

# Task 24 start
# Escape Characters
txt_55 = "We are the so-called \"Vikings\" from the north"
print(txt_55)
# Task 24 end

# Task 25 start
# Python Booleans
a = 200
b = 33
if b > a:
    print("b greater than a.")
else:
    print("b isn`t greater than a.")
# Task 25 end