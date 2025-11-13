# Check palindrome number.

def palindrome(number):
    print("Original number", number)
    original_num = number

# reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

# check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not paliandrome.")

palindrome(121)
palindrome(125)
palindrome(525)

def is_palindrome(number):
    # handle negative numbers (they are typically not palindrome)
    if number < 0:
        return False
    
    # convert the number to a string
    original_string = str(number)

    # reverse the string using slicing
    reversed_string = original_string[::-1]

    # compare the original and reversed strings
    if original_string == reversed_string:
        return True
    else:
        return False
    
# example usage
print(is_palindrome(121)) # output: True
print(is_palindrome(123)) # output: False
print(is_palindrome(525)) # output: True
print(is_palindrome(274)) # output: False