# Aaron Fox
# CECS 563
# Assignment 2 Problem 2
# Calculates the number of involutory keys in the English language (Zsub26)

# Just a simple factorial function
def factorial(num):
    product = 1
    while num > 1:
        product = product * num
        num = num - 1
    return product
        
def calculate_involutary_keys(n):
    total = 0
    # e.g. cycles of 2, 1, 1, ..., 1 and 2, 2, 1, 1, ..., 1 are all involutory keys
    for i in range(2, n + 1):
        if i % 2 == 0:
            print("i == " + str(i))
            result = (factorial(26) / factorial(26 - i)) / (2 ** (i / 2) * factorial(i / 2))
            # print("result == " + str(result))
            
            print(f"{int(result):,d}")
            total = total + result
    return total

# Sample of what variables were involved in the result
# English alphabet is just Zsub26
total = calculate_involutary_keys(26)
print("total == " + str(total))
