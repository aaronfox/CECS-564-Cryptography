# Aaron Fox
# Project 1 (Binary Vigenere Crypto System)
# CECS 564
# Dr. Desoky
# NOTE: The encoding here uses extended ASCII-256 encoding based on the Windows-1252 encoding found at:
# this means that the following results from using the chr function, following the extended ASCII
# table found here: https://www.ascii-code.com/
# chr(250) == ú
# chr(251) == û
# chr(252) == ü
# chr(253) == ý
# chr(254) == þ
# chr(255) == ÿ

# encrypt_vigenere
# NOTE: This uses Windows-1252 Extended ASCII Encoding
# Standard encodings are referenced here: https://docs.python.org/2.4/lib/standard-encodings.html
# INPUT: text_file_path: (string) filepath of text file
# OUTPUT: Encrypted .txt file that is saved to the current folder
def encrypt_vigenere(text_file_path, key):
    # Open ASCII text file for reading based on input path
    text_file = open(text_file_path, 'r') # windows-1252 is extended ascii 256
    # Read all info
    text = text_file.read()
    text_file.close()

    index = 0
    encrypted_text = []
    # m is the key length, as specified by the Project 2 prompt formula
    m = len(key)

    # Encrypt file here
    encrypted_file = open("fox_encrypted_vigenere_file.txt", "w", encoding="utf-8")
    while index < len(text):
        # Append encrypted text into large array of characters
        
        # ascii_value = bytes(text[index], encoding='windows-1252').decode('windows-1252').encode('windows-1252', 'backslashreplace') 
        ascii_value = ord(text[index])
        # key_value = bytes(key[index % m], encoding='windows-1252').decode('windows-1252')
        key_value = ord(key[index % m])
        encrypted_value = (ascii_value + key_value) % 256

        # Can use this for loop to show that the proper encoding is being used here
        # for i in range(256):
        #     print("chr(" + str(i) + ") == " + chr(i))
        
        # value = (ascii_value + key_value) % 256
        # encrypted_text.append(chr(ascii_value))
        print('ascii_value == ' + str(ascii_value))
        print('key_value == ' + str(key_value))
        print('encrypted_value == ' + str(encrypted_value))
        print("chr(" + str(encrypted_value) + ") == " + chr(encrypted_value))
        encrypted_text.append(chr(encrypted_value))

        # Increment index each time to continue encrypting
        index = index + 1
        # Place value into output file
        encrypted_file.write(chr(encrypted_value))

    encrypted_file.close()
    # Encrypt text using vigenere method
    
    # Join encrypted characters into one string
    print(''.join(encrypted_text))

    # Encrypt string using 

if __name__== "__main__":
    print("Encrypting text using Vigenere enccryption...")
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\MansNotHot.txt"
    encryption_key='donoteatmeplease'
    encrypt_vigenere(text_file_path=file_path, key=encryption_key)
