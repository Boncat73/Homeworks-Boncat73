# Given two integer numbers, write a Pythin program to return their
# product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

def function(num1, num2):
    res1 = num1 * num2

    if res1 <= 1000:
        return res1
    else:
        return num1 + num2
    
result = function(10, 20)
print("The result is ", result)

result = function( 90, 90)
print("The result is ", result)


