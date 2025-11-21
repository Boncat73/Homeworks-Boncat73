# A Prime Number is a number that can only be divided by itself 
# and 1 without remainders (e.g., 2, 3, 5, 7, 11).
# function to check if a number is prime
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
# Alternate prime numbers from 1 to 20: 2, 5, 11, 17

number = [2, 3, 5, 7, 11, 13, 17, 19]

# function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Set N
N = 20
primes = [] # list to store all prime numbers
for number in range(2, N + 1):
    if is_prime(number):
        primes.append(number)

# Print all prime numbers
print(f"Prime all numbers from 1 to {N}: {primes}")

# Print alternate prime numbers from the list
print(f"Alternate prime numbers from 1 to {N}:")
for i in range(0, len(primes), 2): # step by 2 to get alternate primes
    print(primes[i])