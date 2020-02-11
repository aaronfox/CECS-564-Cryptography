# Aaron Fox
# Project 1 (Binary Vigenere Crypto System)
# CECS 564
# Dr. Desoky

# encrypt_vigenere
# INPUT: text_file_path: (string) filepath of text file
# OUTPUT: Encrypted .txt file that is saved to the current folder
def encrypt_vigenere(text_file_path, key):
    # Open ASCII text file for reading based on input path
    text_file = open(text_file_path, 'r', encoding='ascii')
    # Read all info
    text = text_file.read()
    text_file.close()

    index = 0
    encrypted_text = []
    # Encrypt file here
    while index < len(text):
        # Append encrypted text into large array of characters
        encrypted_text.append(text[index])
        # Increment index each time to continue encrypting
        index = index + 1
    
    # Join encrypted characters into one string
    print(''.join(encrypted_text))

    # 

if __name__== "__main__":
    print("Encrypting text using Vigenere enccryption...")
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\MansNotHot.txt"
    encryption_key='donoteatmeplease'
    encrypt_vigenere(text_file_path=file_path, key=encryption_key)
