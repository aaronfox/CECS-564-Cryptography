# Prototype Linear-Feedback Shift Register method that will
# be replaced by the generator method below it
# INPUT: taps: The equivalent primitive polynomial used (e.g. for polynomial x^15 + x + 1, taps=[15, 1])
#        seed: Seed of LSFR to be used in binary, e.g. 40 bit key of '0001100111100110000000110100000000001100'
# OUTPUT: None (just prints)
def LFSR(taps, seed):
    print("With initialization vector (" + seed[0] + ", " + seed[1] + ", " + seed[2] + ", " + seed[3] + "):")
    s = seed
    xor_output = 0

    init_pass = 0
    cycle_length = 0
    print(s)
    while (s != seed or init_pass == 0):# and cycle_length < 5:
        cycle_length = cycle_length + 1
        init_pass = 1
        for tap in taps:
            # print("int(s[len(s)-tap]) == " + str(int(s[len(s)-tap])))
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

LFSR([4, 1], '1111')
