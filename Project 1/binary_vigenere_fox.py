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
def get_probability_dist_of_text(filepath_of_text_to_get_pdf_from):
    print("Getting PDF of text...")
    text_file = open(filepath_of_text_to_get_pdf_from, "r", encoding="latin1")

    # Build out each character in Z_256 of probabilities dictionary with a count of 0 initially
    probabilities_dict = {}
    for i in range(0, 256):
        probabilities_dict[chr(i)] = 0

    # Record total number of characters for calculating the probability distribution 
    total_number_of_characters = 0
    while True:
        # Read one character at a time
        char = text_file.read(1)
        if not char:
            break
        if char in probabilities_dict:
            probabilities_dict[char] = probabilities_dict[char] + 1
            total_number_of_characters = total_number_of_characters + 1
        else:
            print("Skipping character " + str(char) + ", because it is not in the extended ASCII table")

    # Before getting probability, save it in the letter_count_dict
    # for finding the index of coincidence of each letter
    letter_count_dict = probabilities_dict.copy()

    # Get percentage of each characters usage
    for i in range(0, 256):
        probabilities_dict[chr(i)] = probabilities_dict[chr(i)] / total_number_of_characters

    # graph_probability_of_each_character(probabilities_dict)

    return [probabilities_dict, letter_count_dict]
    
           

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
    [probabilities_dict, letter_count_dict] = get_probability_dist_of_text(typical_text)
    # # Attacking encrypted file
    ioc = get_index_of_coincidence(unencrypted_text)
    print("ioc == " + str(ioc))

    multiple_iocs = get_multiple_iocs(64, encrypted_text)
    graph_iocs(multiple_iocs)


