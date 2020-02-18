# get_text returns a string of the text contained within a text file
# INPUT: file_path (string): filepath of text to turn into a string
# OUTPUT: output_text (string): string of all text contained inside filepath
def get_text(file_path):
    text = open(file_path, "r", encoding="latin1")
    output_text = []
    while True:
        # Read one character at a time
        c = text.read(1)
        if not c:
            break
        output_text.append(c)

    output_text = ''.join(output_text)
    return output_text

# Returns modal character of given text
# NOTE: It will only return one character even if there is more than one
def get_mode(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1

    print(ord(max(char_dict, key=char_dict.get)))
    return max(char_dict, key=char_dict.get)

# def get_median

if __name__ == "__main__":
    unencrypted_text = get_text(r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\The_Lottery_Shirley_Jackson.txt")
    encrypted_text = get_text(r"C:\Users\aaron\Classes_11th_Semester\CECS 564\CECS-564-Cryptography\Project 1\fox_encrypted_vigenere_file_the_lottery.txt")

    print("Modal char of unencrypted_text == " + str(get_mode(unencrypted_text)))
    print("Modal char of encrypted_text == " + str(get_mode(encrypted_text)))
