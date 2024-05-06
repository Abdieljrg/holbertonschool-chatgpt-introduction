#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number using recursion.

# Parameters:
# - n: An integer representing the number whose factorial is to be calculated.

# Returns:
# - The factorial of the input number 'n'.
def factorial(n):
    # Base case: If the input number is 0, return 1.
    if n == 0:
        return 1
    else:
        # Recursive case: Multiply the input number by the factorial of (n-1).
        return n * factorial(n-1)

# Calculate the factorial of the integer passed as a command-line argument.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial.
print(f)