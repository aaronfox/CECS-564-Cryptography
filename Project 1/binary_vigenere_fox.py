# Aaron Fox
# Project 1 (Binary Vigenere Crypto System)
# CECS 564
# Dr. Desoky
# NOTE: The encoding here uses extended ASCII-256 encoding based on the first 256 characters UTF-8 encoding found at:
# this means that the following results from using the chr function, following the extended ASCII
# table found here: https://www.ascii-code.com/
# chr(252) == ü
# chr(253) == ý
# chr(254) == þ
# chr(255) == ÿ

# For directory usage (os.getcwd)
import os

# encrypt_vigenere encrypts the text in a given filepath and outputs it to the given filepath
# NOTE: This uses the first 256 characters of UTF-8, which is equivalent 
# INPUT: text_file_path (string): filepath of file containing extended ASCII text to be encrypted
#        key (string): key that is to be used to encrypt the text
#        output_file_name (string): just the file name of the output file to be placed in the current directory
# OUTPUT: None. But saves encrypted .txt file to the current directory
def encrypt_vigenere(text_file_path, key, output_file_name):
    print("Encrypting text using Vigenere encryption...")
    # Open ASCII text file for reading based on input path
    text_file = open(text_file_path, 'r', encoding='utf-8') # windows-1252 is extended ascii 256
    # Read all info
    text = text_file.read()
    text_file.close()

    index = 0
    encrypted_text = []
    # m is the key length, as specified by the Project 2 prompt formula
    m = len(key)

    # Encrypt file here
    encrypted_file = open(output_file_name, "w", encoding="utf-8")
    while index < len(text):
        # Append encrypted text into large array of characters
        
        # Yi = (Xi + Ki % m) % 256
        X_i = ord(text[index])
        K_i = ord(key[index % m])
        Y_i = (X_i + K_i) % 256

        # Can use this for loop to show that the proper encoding is being used here
        # for i in range(256):
        #     print("chr(" + str(i) + ") == " + chr(i))
        
        # Debugging (Uncomment for testing purposes)
        # print('X_i == ' + str(X_i))
        # print('K_i == ' + str(K_i))
        # print('Y_i == ' + str(Y_i))
        # print("chr(" + str(Y_i) + ") == " + chr(Y_i))
        # encrypted_text.append(chr(Y_i))

        # Increment index each time to continue encrypting
        index = index + 1
        # Place value into output file
        encrypted_file.write(chr(Y_i))

    encrypted_file.close()
    print("Successfully encrypted text. It is stored in " + str(os.getcwd()) + "\\" + str(output_file_name))
    # Encrypt text using vigenere method
    
    # Join encrypted characters into one string
    # print(''.join(encrypted_text))


# Decrypt the text found in the filepath of filepath_of_encrypted based on the Vigenere Cipher
# INPUT: filepath_of_encrypted (string): whole filepath file to be encrypted
#        key (string): key that was used to encrypt the text
#        output_file_name (string): just the file name of the output file to be placed in the current directory
# OUTPUT: None. But saves decrypted .txt file to the current directory
def decrypt_vigenere(filepath_of_encrypted, key, output_file_name):
    print("Decrypting text using Vigenere process...")
    encrypted_text = open(filepath_of_encrypted, 'r', encoding='utf-8')
    decrypted_text_file = open(output_file_name, 'w', encoding='utf-8')
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
        


if __name__== "__main__":
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\MansNotHot.txt"
    encryption_key='pineapple'
    encrypt_vigenere(text_file_path=file_path, key=encryption_key, output_file_name="fox_encrypted_vigenere_file.txt")
    encrypted_file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\fox_encrypted_vigenere_file.txt"
    decrypt_vigenere(filepath_of_encrypted=encrypted_file_path, key=encryption_key, output_file_name="fox_decrypted_text.txt")
