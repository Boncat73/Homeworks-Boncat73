# Write a Python code to remove characters from 
# a string from 0 to n and return a new string.

# create a function and pass two arguments: a string and the 
# number of characters to remove from the beginning of the string
def remove_chars(word, n): 
    print('Original string:', word) # print the original string
    x = word[n:] # use a string slice from character n to the end of the string
    return x # the function returns the new string as part of the original

# print the result
print("Removing characters form s string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

