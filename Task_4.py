import math
import random

# Initialize variables
num_1 = 0
operation = ""
num_2 = 0
result = None  # Use None to detect invalid cases

# Take inputs
num_1 = int(input("Enter the 1st number: "))
num_2 = int(input("Enter the 2nd number: "))
operation = input("Enter one of: bitwise or, bitwise and, bitwise xor, generate random, percentage, square root: ")

# Perform operations
if operation == "bitwise or":
    result = num_1 | num_2

elif operation == "bitwise and":
    result = num_1 & num_2

elif operation == "bitwise xor":
    result = num_1 ^ num_2

elif operation == "generate random":
    # Ensure num_1 <= num_2 for randint
    low = min(num_1, num_2)
    high = max(num_1, num_2)
    result = random.randint(low, high)

elif operation == "percentage":
    if num_2 != 0:
        result = (num_1 / num_2) * 100
    else:
        print("Error: Cannot divide by zero.")

elif operation == "square root":
    if num_1 >= 0:
        result = math.sqrt(num_1)
    else:
        print("Error: Cannot take square root of a negative number.")

else:
    print("Invalid operation selected.")

# Final output
if result is not None:
    print(f"Result: {result}")
