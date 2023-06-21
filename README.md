# DNA-Converter
Simple Text->DNA and DNA->Text Converters

by: Obaida Ismail

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
