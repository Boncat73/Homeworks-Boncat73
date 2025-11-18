# A palindrome number is a number that remains the same 
# when its digits are reversed. In simpler terms, it 
# reads the same forwards and backward. For example 121, 5005.

# define a function
def is_palindrome(number):
    # initialize a variable to store the reversed number (set it to 0 initially)
    original_number = number
    reversed_number = 0

    # use a while loop that continues as long as the original number is greater than 0
    while number > 0:
        # extract the last digit of the original number using the modulo operator (% 10)
        remainder = number % 10
        # update the reversed number: multiply it by 10 and then add the extracted last digit
        reversed_number = (reversed_number * 10) + remainder
        # update the original number by integer division (//10) to remove the last digit
        number //= 10

    # after the loop finishes, the reversed number variable will hold the reversed integer
    return original_number == reversed_number

# to check if it is same as original number
print(is_palindrome(121)) # output: True
print(is_palindrome(123)) # output: False
