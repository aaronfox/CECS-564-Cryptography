# Aaron Fox
# Project 1 (Binary Vigenere Crypto System)
# CECS 564
# Dr. Desoky
# NOTE: The encoding here uses extended ASCII-256 encoding based on the first 256 characters latin1 (iso-8859-1) encoding found at:
# this means that the following results from using the chr function, following the extended ASCII
# table found here: https://www.ascii-code.com/
# chr(252) == ü
# chr(253) == ý
# chr(254) == þ
# chr(255) == ÿ

# For directory usage (os.getcwd)
import os
# For graphing frequency distributions
import matplotlib.pyplot as plt
# For math.floor
import math

# encrypt_vigenere encrypts the text in a given filepath and outputs it to the given filepath
# NOTE: This uses the first 256 characters of latin1, which is equivalent 
# INPUT: text_file_path (string): filepath of file containing extended ASCII text to be encrypted
#        key (string): key that is to be used to encrypt the text
#        output_file_name (string): just the file name of the output file to be placed in the current directory
# OUTPUT: [unencrypted_text, encrypted_text] But saves encrypted .txt file to the current directory
def encrypt_vigenere(text_file_path, key, output_file_name):
    print("Encrypting text using Vigenere encryption...")
    # Open ASCII text file for reading based on input path
    text_file = open(text_file_path, 'r', encoding='latin1')
    # Read all info of  extended ASCII characters only
    text = []
    i = 0
    while True:
        # Read one character at a time, including only chars of first 256 characters
        char = text_file.read(1)
        if not char:
            break
        if ord(char) > 0 and ord(char) < 256:
            text.append(char)
        else:
            print("Excluding char " + str(char) + " from reading of input file because its not in ASCII-256")
        i = i + 1
    text_file.close()

    index = 0
    # m is the key length, as specified by the Project 1 prompt formula
    m = len(key)

    encrypted_text= []
    # Encrypt file here
    encrypted_file = open(output_file_name, "w", encoding="latin1")
    while index < len(text):
        # Yi = (Xi + Ki % m) % 256
        X_i = ord(text[index])
        K_i = ord(key[index % m])
        Y_i = (X_i + K_i) % 256

        # Increment index each time to continue encrypting
        index = index + 1
        # Place value into output file
        encrypted_file.write(chr(Y_i))

        # Debugging (Uncomment for testing purposes)
        # print('X_i == ' + str(X_i))
        # print('K_i == ' + str(K_i))
        # print('Y_i == ' + str(Y_i))
        # print("chr(" + str(Y_i) + ") == " + chr(Y_i))
        encrypted_text.append(chr(Y_i))

    encrypted_file.close()
    print("Successfully encrypted text. It is stored in " + str(os.getcwd()) + "\\" + str(output_file_name))
    return [''.join(text), ''.join(encrypted_text)]


# Decrypt the text found in the filepath of filepath_of_encrypted based on the Vigenere Cipher
# INPUT: filepath_of_encrypted (string): whole filepath file to be encrypted
#        key (string): key that was used to encrypt the text
#        output_file_name (string): just the file name of the output file to be placed in the current directory
# OUTPUT: None. But saves decrypted .txt file to the current directory
def decrypt_vigenere(filepath_of_encrypted, key, output_file_name):
    print("Decrypting text using Vigenere process...")
    encrypted_text = open(filepath_of_encrypted, 'r', encoding='latin1')
    decrypted_text_file = open(output_file_name, 'w', encoding='latin1')
    index = 0
    m = len(key)
    while True:
        # Read one character at a time
        char = encrypted_text.read(1)
        if not char:
            break

        # Xi = (Yi – Ki % m) % 256
        Y_i = ord(char)
        K_i = ord(key[index % m])
        X_i = (Y_i - K_i) % 256
        index = index + 1

        decrypted_text_file.write(chr(X_i))

    decrypted_text_file.close()
    print("Successfully decrypted text. It is stored in " + str(os.getcwd()) + "\\" + str(output_file_name))

# graph_probability_of_each_character plots a probability bar chart of each character in a text
# INPUT: dictionary (dict): key: letter, value: probability
# OUTPUT: None, just displays a graph
def graph_probability_of_each_character(probabilities_dict):
    # Display bar chart of probabilities of each letter, ignoring characters that aren't in text
    plotting_values = {}
    for key, val in probabilities_dict.items():
        if val != 0:
            plotting_values[key] = val

    plt.bar(plotting_values.keys(), plotting_values.values())
    plt.xlabel('Character')
    plt.ylabel('Probability')
    plt.title('Probability of each character in a typical Text file')
    # plt.show()


# get_index_of_coincidence returns the index of coincence IOC) of a text
def get_index_of_coincidence(text):
    # Calculate frequency of each char
    char_frequency = {}
    for i in range(255):
        char_frequency[chr(i)] = 0

    for char in text:
        char_frequency[char] = char_frequency[char] + 1

    sum = 0
    N = len(text)
    for key in char_frequency.keys():
        sum = sum + (char_frequency[key] * (char_frequency[key] - 1))

    return sum / (N * (N - 1))


# get_multiple_iocs gets multiple iocs from the text based on various sizes of keywords
# e.g. get every second letter, every third letter, every fourth letter
# and determine how that influences the IOC
# INPUT: num_to_stop (int): number to stop checking of every nth letter to slice out
#        text (string): text to analyze the IOCs from
# OUTPUT: iocs (list): ordered list of IOCs from 2 to num_to_stop
def get_multiple_iocs(num_to_stop, text):
    iocs = []
    for i in range(2, num_to_stop):
        new_text = []
        for i in range(0, len(text), i):
            new_text.append(text[i])

        ioc = get_index_of_coincidence(''.join(new_text))
        iocs.append(ioc)
    return iocs

# graph_iocs simply graphs out the iocs
def graph_iocs(iocs):
    x = list(range(2, 2 + len(iocs)))
    plt.bar(x, iocs)
    plt.xlabel('Assumed Key Length')
    plt.ylabel('IOC')
    plt.title('IOCs of Assumed Key Lengths')
    plt.show()


# get_probability_dist_of_text gets the probability density function of a typical text file
# OUTPUT: [probabilities_dict (dict), letter_count_dict (dict)]: An array containing a 
# dictionary with each extended ASCII character and the probability of that character occuring and 
# a dictionary with the count of each letter
def get_probability_dist_of_text(value_to_increment_letter_by, filepath_of_text_to_get_pdf_from):
    print("Getting probability distribution of text...")
    text_file = open(filepath_of_text_to_get_pdf_from, "r", encoding="latin1")

    # Build out each character in Z_256 of probabilities dictionary with a count of 0 initially
    probabilities_dict = {}
    for i in range(0, 256):
        probabilities_dict[chr((i + value_to_increment_letter_by) % 256)] = 0

    # Record total number of characters for calculating the probability distribution 
    total_number_of_characters = 0
    while True:
        # Read one character at a time, incrementing by certain value
        char = text_file.read(1)
        if not char:
            break
        else:
            char = chr((ord(char) + value_to_increment_letter_by) % 256)

        if char in probabilities_dict:
            probabilities_dict[char] = probabilities_dict[char] + 1
            total_number_of_characters = total_number_of_characters + 1
        else:
            print("Skipping character " + str(char) + ", because it is not in the extended ASCII table + value_to_increment_letter_by")

    # Before getting probability, save it in the letter_count_dict
    # for finding the index of coincidence of each letter
    letter_count_dict = probabilities_dict.copy()

    # Get percentage of each characters usage
    for i in range(0, 256):
        probabilities_dict[chr((i + value_to_increment_letter_by) % 256)] = probabilities_dict[chr((i + value_to_increment_letter_by) % 256)] / total_number_of_characters

    # graph_probability_of_each_character(probabilities_dict)

    return [probabilities_dict, letter_count_dict]
    
  

# break_caesar_cipher uses the Chi-squared method to help determine the lowest Chi-squared
# value which should correspond to the value which should crack the given cipher
# NOTE: For project 1, it is assumed that the key is only of lowercase alphabetic letters
def break_caesar_cipher(encrypted_text, key_length, starting_letter_index):
    text_to_be_evaluated = []
    print("len(encrypted_text) == " + str(len(encrypted_text)))

    # Append every nth letter beginning from 0, where n is every key_length letter
    for i in range(math.floor(len(encrypted_text) / key_length)):
        text_to_be_evaluated.append(encrypted_text[i * key_length + starting_letter_index])

    text_to_be_evaluated = ''.join(text_to_be_evaluated)
    print("len(text_to_be_evaluated) == " + str(len(text_to_be_evaluated)))
    first_letter = text_to_be_evaluated[0]

    # print("text_to_be_evaluated[0:5] == " + str(text_to_be_evaluated[0:5]))

    # Get chi-squared values of all sequences
    # Sum from Z=0 to Z=255((C_i - E_i)^2 / E_i)
    chi_squared_values = []

    lowest_chi_squared = float("inf")
    lowest_values = []
    debug_file = open(r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\debug_file.txt", "w", encoding="latin1")
    [probabilities_dict, _] = get_probability_dist_of_text(0, r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\The_Lottery_Shirley_Jackson.txt")
    
    value_to_increment_letter_by_with_highest_valid_letter_count = 0
    highest_num_valid_letter_count = 0
    # Then iterate over every possible sequence
    # e.g. for text_to_be_evaluated = ACB, evaluate BDC, CED, etc.
    for value_to_increment_letter_by in range(0, 256):
        # Make sure text_to_be_evaluated is correctly manipulated with Caesar cipher first
        new_text_to_be_evaluated = []
        for i in range(len(text_to_be_evaluated)):
            new_text_to_be_evaluated.append(chr((ord(text_to_be_evaluated[i]) + value_to_increment_letter_by) % 256))

        new_text_to_be_evaluated = ''.join(new_text_to_be_evaluated)
        debug_file.write(str(new_text_to_be_evaluated))

        total_num_chars_in_text = 0
        for v in probabilities_dict.values():
            total_num_chars_in_text = total_num_chars_in_text + v

        # print("new_text_to_be_evaluated[0:5] == " + str(new_text_to_be_evaluated[0:5]))
        # First, get count of each letter in a dict
        freq_dict_for_sequence = {}
        for i in range(0, 256):
            freq_dict_for_sequence[chr(i)] = 0

        for char in new_text_to_be_evaluated:
            freq_dict_for_sequence[char] = freq_dict_for_sequence[char] + 1
        
        debug_file.write("\n\n" + str(freq_dict_for_sequence) + "\n\n")


        # Then, use that frequency dictionary along with the expected count of the letters 
        # to find the chi-squared values
        chi_squared_sum = 0
        num_valid_letters = 0
        for char in freq_dict_for_sequence.keys():
            # First, make sure character is in new text
            if freq_dict_for_sequence[char] != 0:
                # If that char is an english letter, then carry on, else penalize
                if probabilities_dict[char] != 0:
                    chi_squared_sum = chi_squared_sum + ((freq_dict_for_sequence[char] - total_num_chars_in_text * probabilities_dict[char]) ** 2) / (total_num_chars_in_text * probabilities_dict[char])
                    num_valid_letters = num_valid_letters + 1
                else:
                    penalty_value_for_not_english_letter = 10000
                    chi_squared_sum = chi_squared_sum + penalty_value_for_not_english_letter
        print(str(value_to_increment_letter_by) +".) chi_squared_sum == " + str(chi_squared_sum))
        debug_file.write("\n\n" +str(value_to_increment_letter_by) + ".) chi_squared_sum == " + str(chi_squared_sum) + "\n")
        debug_file.write("\n" + "num_valid_letters == " + str(num_valid_letters) + "\n")
        if lowest_chi_squared > chi_squared_sum:
            lowest_chi_squared = chi_squared_sum
            lowest_values = str(value_to_increment_letter_by) +".) chi_squared_sum == " + str(chi_squared_sum)
        if highest_num_valid_letter_count < num_valid_letters:
            value_to_increment_letter_by_with_highest_valid_letter_count = value_to_increment_letter_by
            highest_num_valid_letter_count = num_valid_letters
    
    print("lowest_values == " + str(lowest_values))
    print("lowest_chi_squared == " + str(lowest_chi_squared))
    print("highest num_valid_letters == " + str(highest_num_valid_letter_count))
    equivalent_ascii = chr(97 + (159 - value_to_increment_letter_by_with_highest_valid_letter_count))
    # print("highest value_to_increment_letter_by_with_highest_valid_letter_count == " + str(value_to_increment_letter_by_with_highest_valid_letter_count) + ", or " + str(chr(value_to_increment_letter_by_with_highest_valid_letter_count - 32)))
    print("equivalent_ascii == " + equivalent_ascii)
    debug_file.close()
    return equivalent_ascii

# attack_vigenere_cipher attacks the text of a file encrypted with the Vigenere cipher
def attack_vigenere_cipher(filepath_of_encrypted_file):
    print("Attacking file encrypted with Vigenere cipher...")

if __name__== "__main__":
    # Encrypting file
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\MansNotHot.txt"
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\The_Lottery_Shirley_Jackson.txt"
    encryption_key='pineapple'
    [unencrypted_text, encrypted_text] = encrypt_vigenere(text_file_path=file_path, key=encryption_key, output_file_name="fox_encrypted_vigenere_file.txt")

    # # Decrypting file
    encrypted_file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\fox_encrypted_vigenere_file.txt"
    encrypted_file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\encrypted.txt"
    # encrypted_file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\message_to_decrypt_from_teammate.txt"
    encryption_key = "cthulhu"
    decrypt_vigenere(filepath_of_encrypted=encrypted_file_path, key=encryption_key, output_file_name="fox_decrypted_text.txt")

    # Obtaining probability distribution of a typical text
    typical_text = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\The_Lottery_Shirley_Jackson.txt"
    [probabilities_dict, letter_count_dict] = get_probability_dist_of_text(0, typical_text)
    # # Attacking encrypted file
    ioc = get_index_of_coincidence(unencrypted_text)
    print("ioc == " + str(ioc))

    multiple_iocs = get_multiple_iocs(64, encrypted_text)
    # graph_iocs(multiple_iocs)

    # Analyzing the IOC graph above for the assumed key lengths, we can determine the length of the key
    # based on the (probably) least common multiple of all the occurring spikes
    # (e.g. if the key is 9 letters long, there is an IOC spike every 9th assumed key length in the graph)
    analyzed_key_length_from_graph = 9

    # Once we know the length of the key, the problem is effectively the same as solving the Caesar Cipher
    # Problem. So we can use the Chi-squared calculations to solve for the letters of the key
    # (The lowest chi-squared is most likely to be the key, although it is not guaranteed)
    # There are thus analyzed_key_length_from_graph Caesar ciphers to break

    encrypted_text_filepath = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\encrypted.txt"
    
    encrypted_text = open(encrypted_text_filepath, "r", encoding="latin1")
    text = []
    while True:
        # Read one character at a time
        c = encrypted_text.read(1)
        if not c:
            break
        text.append(c)

    encrypted_text = ''.join(text)
        
    analyzed_key_length_from_graph = 7
    keyword = []
    for i in range(0,analyzed_key_length_from_graph):
        keyword.append(break_caesar_cipher(encrypted_text, analyzed_key_length_from_graph, i))

    print("keyword:" + ''.join(keyword))


