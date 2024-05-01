def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            if mode == "encrypt":
                char_code += shift
            elif mode == "decrypt":
                char_code -= shift
            result += chr(char_code % 26 + ascii_offset)
        else:
            result += char
    return result

def text_to_binary(text):
    return " ".join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return "".join(chr(int(binary_code, 2)) for binary_code in binary.split())

def double_encryption(text, shift1, shift2):
    encrypted_text = caesar_cipher(text, shift1, "encrypt")
    return caesar_cipher(encrypted_text, shift2, "encrypt")

def double_decryption(text, shift1, shift2):
    decrypted_text = caesar_cipher(text, shift2, "decrypt")
    return caesar_cipher(decrypted_text, shift1, "decrypt")

def main():
    while True:
        print("Caesar Cipher Tool")
        print("------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Encrypt to Binary")
        print("4. Decrypt from Binary")
        print("5. Double Encryption")
        print("6. Double Decryption")
        print("7. Double Decryption with shifts 1-10")
        print("8. Exit")
        print("9. Help")

        choice = input("Choose an option: ")

        if choice in ["1", "2"]:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            if choice == "1":
                print("Encrypted text: ", caesar_cipher(text, shift, "encrypt"))
            else:
                for i in range(1, 11):
                    print(f"Decrypted text with shift {i}: {caesar_cipher(text, i, 'decrypt')}")
        elif choice == "3":
            text = input("Enter the text: ")
            print("Binary text: ", text_to_binary(text))
        elif choice == "4":
            binary = input("Enter the binary text: ")
            print("Decrypted text: ", binary_to_text(binary))
        elif choice == "5":
            text = input("Enter the text: ")
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            print("Double encrypted text: ", double_encryption(text, shift1, shift2))
        elif choice == "6":
            text = input("Enter the text: ")
            shift1 = int(input("Enter the first shift value: "))
            shift2 = int(input("Enter the second shift value: "))
            print("Double decrypted text: ", double_decryption(text, shift1, shift2))
        elif choice == "7":
            text = input("Enter the text: ")
            for shift1 in range(1, 11):
                for shift2 in range(1, 11):
                    print(f"Double decrypted text with shifts {shift1} and {shift2}: {double_decryption(text, shift1, shift2)}")
        elif choice == "8":
            break
        elif choice == "9":
            print("Help:")
            print("Encrypt: Shifts the text forward by the shift value.")
            print("Decrypt: Shifts the text backward by the shift value.")
            print("Encrypt to Binary: Converts the text to binary format.")
            print("Decrypt from Binary: Converts the binary text back to normal text.")
            print("Double Encryption: Encrypts the text twice with two different shift values.")
            print("Double Decryption: Decrypts the text twice with two different shift values.")
            print("Double Decryption with shifts 1-10: Decrypts the text with all possible combinations of shifts 1-10 for both the first and second shifts.")
            print("Shift value: The number of positions to shift the text.")
        else:
            print("Denis Dalbayoba. Please choose a valid option.")

if __name__ == "__main__":
    main()