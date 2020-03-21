# Aaron Fox
# CECS 564
# Spring 2020
# Dr Desoky

def LFSR(taps, seed):
    s = seed
    xor_output = 0

    init_pass = 0
    cycle_length = 0
    print(s)
    while (s != seed or init_pass == 0):# and cycle_length < 5:
        cycle_length = cycle_length + 1
        init_pass = 1
        for tap in taps:
            xor_output = xor_output + int(s[len(s)-tap])
            # xor_output = xor_output + int(s[tap-1])
            
        if xor_output % 2 == 0.0:
            xor_output = 0
        else:
            xor_output = 1
        s = str(xor_output) + s[0:len(s) - 1]
        xor_output = 0
        print(s)
    # Print out final seed also to show cycle
    print(s)
    print("Cycle length: " + str(cycle_length))


# Generator function so state of local variables is saved and can 
# continue running but it yields the next shifted bit to be used
# by the full adder
def LFSR_generator(taps, seed):
    s = seed
    xor_output = 0
    yield s[len(s)-1]
    while 1:#(s != seed or init_pass == 0):  # and cycle_length < 5:
        for tap in taps:
            xor_output = xor_output + int(s[len(s)-tap])
        if xor_output % 2 == 0.0:
            xor_output = 0
        else:
            xor_output = 1
        s = str(xor_output) + s[0:len(s) - 1]
        xor_output = 0
        yield s[len(s)-1]

# This code shows how each bit can be generated in bytes (8 bits at a time)
# test_gen = LFSR_generator((4, 1), '0001')
# for i in range(48):
#     if i % 8 == 0:
#         print()
#     print(next(test_gen), end='')

# Converts a string of binary letters to an integer in decimal
# INPUT: Takes in a text string of binary numbers
# OUTPUT: Outputs an integer decimal number of the equivalent decimal of the input binary string
def binary_to_decimal(binary):
    decimal = 0
    print(type(binary))
    for i in range(len(binary)):
        decimal = decimal + int(binary[len(binary) - 1  - i]) * 2 ** i
    return decimal

# print(binary_to_decimal("01011001"))
# binary_to_decimal(101)
# Code for 8 bit full adder STARTS here

# Half adder to be used in full adder
# INPUT: Two bits to be half-added
# OUTPUT: Tuple (sum, carry bit)
# NOTE: ^ is bitwise XOR operator
def half_adder(bit_1, bit_2):
    return (bit_1 ^ bit_2, bit_1 and bit_2)

# Full 
# INPUT: two bits to be full-added and an optional carry bit which defaults to 0
# OUTPUT: Tuple (sum, carry bit)
def full_adder(bit_1, bit_2, carry_bit=0):
    sum_1, carry_1 = half_adder(bit_1, bit_2)
    sum_2, carry_2 = half_adder(sum_1, carry_bit)

    return (sum_2, carry_1 or carry_2)

# Adds to bits of the same length together, rolling over if needed
# This is named 'x_bit_full_adder' because it works for bits of any x length
def x_bit_full_adder(bits_1, bits_2):
    carry_bit = 0
    # Store results into string backwards so that it can be reversed later
    result = ''
    for i in range(len(bits_1) - 1, -1, -1):
        sum_bit, carry_bit = full_adder(int(bits_1[i]), int(bits_2[i]), carry_bit)
        result = result + str(sum_bit)
    # Return result but inverse
    return result[::-1]

def encrypt_css():
    pass

# print(x_bit_full_adder('00111', '00101'))
# Code for 8 bit full adder ENDS here

# R1 LSFR of CSS
# LFSR((15, 1), '00000000000001000')

# R2 LSFR of CSS
# LFSR((15, 5, 4, 1), '0000000000000000000001000')

# LFSR((4, 1), '0001')
# LFSR((4, 3), '0110')
# LFSR((3, 2), '011')
# List of primitive polynomials: http://users.ece.cmu.edu/~koopman/lfsr/index.html
# e.g. for Text file of size of 4 bits, 9 = 1001 = x^4 + x + 1 and C = 1100 = x^4 + x^3 + 1
