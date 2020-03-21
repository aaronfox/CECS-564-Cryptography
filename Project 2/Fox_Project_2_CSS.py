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
    while (s != seed or init_pass == 0) and cycle_length < 5:
        cycle_length = cycle_length + 1
        init_pass = 1
        for tap in taps:
            print("tap-len(s)-1 == " + str(tap-1))
            print("s[tap-1] == " + str(s[tap-1]))
            xor_output = xor_output + int(s[tap-1])
            
        print("after for, xor_output == " + str(xor_output))    
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

# R1 LSFR of CSS
# LFSR((15, 1), '00000000000001000')

# R2 LSFR of CSS
LFSR((15, 5, 4, 1), '0000000000000000000001000')

# LFSR((4, 1), '0001')
# LFSR((4, 3), '0110')
# LFSR((3, 2), '011')
# List of primitive polynomials: http://users.ece.cmu.edu/~koopman/lfsr/index.html
# e.g. for Text file of size of 4 bits, 9 = 1001 = x^4 + x + 1 and C = 1100 = x^4 + x^3 + 1
