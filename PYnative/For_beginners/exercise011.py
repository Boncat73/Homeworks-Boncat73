# If the given integer number is 7536, the output shall be 6357,
# with a space separating the digits.

number = 7536
print("Given number", number)

while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
    