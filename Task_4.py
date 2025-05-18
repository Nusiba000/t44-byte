num_1 = 0
opreation = 0
num_2 = 0
result =0

num_1 = int(input("Enter the 1st number: "))
num_2 = int(input("Enter the snd number: "))
opreation = input("Enter one of bitwise or, bitwise and,bitwise xor,generate random,percentage,square root: ")


if opreation == "bitwise or":
    result = num_1 | num_2
    print(result)

# Perform Bitwise AND operation
result = num_1 & num_2
print(f"The result of {num_1} & {num_2} is: {result}")