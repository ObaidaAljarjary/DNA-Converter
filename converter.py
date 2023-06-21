"""
Simple Text-to-DNA Converter

Algorithms
TextToDNA:
    - take text_data
    - make two empty string variables: binary_data and dna_data
    - start looping through the text_data :
        - for every character in the text_data:
            - convert the ascci code of character to binary and add it to binary_data
    - convert binary_data into list and split the list into sub list's of length 2
    - start looping through the list:
        - for every sub list :
            - if sub list is equal to '00' add 'A' to dna_data
            - if sub list is equal to '11' add 'T' to dna_data
            - if sub list is equal to '01' add 'C' to dna_data
            - if sub list is equal to '10' add 'G' to dna_data
    - finally return dna_data

DNAtoText:
    - take dna_data
    - make two empty string variables: binary_data and text_data
    - start looping through the dna_data:
        - for every character in the dna_data:
            - if character is equal to 'A' add '00' to binary_data
            - if character is equal to 'T' add '11' to binary_data
            - if character is equal to 'C' add '01' to binary_data
            - if character is equal to 'G' add '10' to binary_data
    - convert binary_data into list and split the list into sub list's of length 7
    - start looping through the binary_data list:
        - for every sub list:
            - convert the sub list from binary to decimal and convert the decimal into character (ascci) and add the character to text_data
    - finally return text_data
"""
def TextToDNA(text_data):
    binary_data = ''
    dna_data = ''
    for char in text_data:
        if len(bin(ord(char))[2:]) == 6:
            binary_data += '0' + bin(ord(char))[2:]
        else:
            binary_data += bin(ord(char))[2:]

    binary_data = [binary_data[i:i + 2] for i in range(0, len(binary_data), 2)]
    for sub in binary_data:
        if sub == '00':
            dna_data += 'A'
        elif sub == '11':
            dna_data += 'T'
        elif sub == '01':
            dna_data += 'C'
        elif sub == '10':
            dna_data += 'G'

    return dna_data


def DNAtoText(dna_data):
    binary_data = ''
    text_data = ''
    for char in dna_data:
        if char == 'A':
            binary_data += '00'
        elif char == 'T':
            binary_data += '11'
        elif char == 'C':
            binary_data += '01'
        elif char == 'G':
            binary_data += '10'

    binary_data = [binary_data[i:i + 7] for i in range(0, len(binary_data), 7)]
    for digit in binary_data:
        text_data += chr(int(digit, 2))

    return text_data


print(TextToDNA("hello from Obaida "))
print(DNAtoText("TCACGCCTCGCGTATCTGGAATATCTAGTCTTGTCCAACATTTACCGACTCATGCATAAGGAA"))
