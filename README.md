# De-EncryptOptions
This code is a simple command-line tool for encrypting and decrypting text using the Caesar Cipher algorithm. Here's a breakdown of the code:
Functions:
caesar_cipher(text, shift, mode): This function implements the Caesar Cipher algorithm. It takes three parameters:
text: the input text to encrypt or decrypt
shift: the shift value to use
mode: either "encrypt" or "decrypt"
The function returns the encrypted or decrypted text.
text_to_binary(text): This function converts text to binary format. It takes one parameter:
text: the input text to convert
The function returns the binary representation of the text.
binary_to_text(binary): This function converts binary text back to normal text. It takes one parameter:
binary: the binary text to convert
The function returns the normal text representation of the binary input.
double_encryption(text, shift1, shift2): This function encrypts the text twice with two different shift values. It takes three parameters:
text: the input text to encrypt
shift1: the first shift value
shift2: the second shift value
The function returns the double-encrypted text.
double_decryption(text, shift1, shift2): This function decrypts the text twice with two different shift values. It takes three parameters:
text: the input text to decrypt
shift1: the first shift value
shift2: the second shift value
The function returns the double-decrypted text.
Main Program:
The main() function is the entry point of the program. It presents a menu to the user with options to:
Encrypt text
Decrypt text
Encrypt text to binary
Decrypt binary text
Double-encrypt text
Double-decrypt text
Double-decrypt text with shifts 1-10
Exit the program
Show help
Based on the user's choice, the program calls the appropriate function and displays the result.
Help:
The help section explains the different options and how they work. It also explains the Caesar Cipher algorithm and the shift value.
