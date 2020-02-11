# Aaron Fox
# Project 1 (Binary Vigenere Crypto System)
# CECS 564
# Dr. Desoky

# encrypt_vigenere
# NOTE: This uses Windows-1252 Extended ASCII Encoding
# Standard encodings are referenced here: https://docs.python.org/2.4/lib/standard-encodings.html
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
    # m is the key length, as specified by the Project 2 prompt formula
    m = len(key)
    # Encrypt file here
    while index < len(text):
        # Append encrypted text into large array of characters
        
        ascii_value = bytes(text[index], encoding='windows-1252').encode('windows-1252') 
        key_value = bytes(key[index % m], encoding='windows-1252').decode('windows-1252')
        print('ascii_value == ' + str(ascii_value))
        # value = (ascii_value + key_value) % 256
        # encrypted_text.append(chr(ascii_value))
        print('ascii_value == ' + str(ascii_value))
        # Debugging:
        print('bytes(text[index], encoding=\'windows-1252\') == ' + str(bytes(text[index], encoding='windows-1252')))
        # print('text[index] == ' + str(text[index]))
        # print('ord(text[index].decode(\'windows-1252\') == ' + str(ord(text[index]).decode('windows-1252')))
        # print('ord(key[index % m].decode(\'windows-1252\') == ' + str(ord(key[index % m]).decode('windows-1252')))
        # print('ascii_value % 256 == ' +
        #       str((ord(text[index]).decode('windows-1252') + ord(key[index % m]).decode('windows-1252')) % 256))
        # print('chr(ascii_value).encode(\'windows-1252\') == ' + chr(ascii_value).encode('windows-1252'))

        # Increment index each time to continue encrypting
        index = index + 1

    
    # Encrypt text using vigenere method
    
    # Join encrypted characters into one string
    print(''.join(encrypted_text))

    # Encrypt string using 

if __name__== "__main__":
    print("Encrypting text using Vigenere enccryption...")
    file_path = r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\MansNotHot.txt"
    encryption_key='donoteatmeplease'
    encrypt_vigenere(text_file_path=file_path, key=encryption_key)
