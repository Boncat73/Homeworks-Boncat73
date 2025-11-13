# Task 1 start
# Create two variables: the first is an integer, the second is a 
# float number as a string. Convert the second number to a float. 
# Add the numbers together, print the result and its type.

num_1 = 5
num_2 = "12.5"

num_2 = float(num_2)
result = num_1 + num_2
print(f"Sum equal: {result}.")
print(f"Type result is {type(result)}.")
# Task 1 end

# Task 2 start
# You have a float variable. Convert her to an int 
# (that is, discard the fractional part). Convert the 
# resulting integer back to str. Print the final value 
# and its type.

num_float = 3.4521
num_float = int(num_float)
num_float = str(num_float)

print(f"Result is: {num_float}")
print(f"Type: {type(num_float)}")
# Task 2 end

# Task 3 start
# String Concatenation. You have an int variable named age. Convert it to str.
# Create a string message using string concatenation that says: 
# "I am [age value] years old." Print the message.

age_person = 52
age_person = str(age_person)
message = "I have " + age_person + " years old."
print(message)
# Task 3 end