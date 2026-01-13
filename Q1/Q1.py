import os

# ///////////  ENCRYPTION FUNCTION ///////////
def encryption(shift1, shift2):
    # opens raw file in read mode and creates (or opens) encrypted file in write mode
    with open("raw_text.txt", "r", encoding="utf-8") as raw_file, \
        open("encrypted_text.txt", "w", encoding="utf-8") as encrypted_file:

        for char in raw_file.read():
            # Encryption logic for lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    # %13 for wrapping around first half of alphabet
                    shift = (shift1 * shift2) % 13
                    # Applying forward shift with wrap around
                    new_char = chr((ord(char) - ord('a') + shift) % 13 + ord('a'))
                else:
                    shift = (shift1 + shift2) % 13
                    # Applying backward shift with wrap around
                    new_char = chr((ord(char) - ord('n') - shift) % 13 + ord('n'))

            # Encryption logic for uppercase letters
            elif char.isupper():
                if 'A' <= char <= 'M':
                    shift = shift1 % 13
                    new_char = chr((ord(char) - ord('A') - shift) % 13 + ord('A'))
                else:
                    shift = (shift2 ** 2) % 13
                    new_char = chr((ord(char) - ord('N') + shift) % 13 + ord('N'))

            # If character is not a letter, no change
            else:
                new_char = char

            encrypted_file.write(new_char)

    print(f"Encryption successfull")

# ///////////  DECRYPTION FUNCTION ///////////
def decryption(shift1, shift2):
    with open("encrypted_text.txt", "r", encoding = "utf-8") as encrypted_file, \
        open("decrypted_text.txt", "w", encoding = "utf-8") as decrypted_file:

        for char in encrypted_file.read():
            # Decryption logic for lowercase letters
            if char.islower():
                if 'a' <= char <= 'm':
                    shift = (shift1 * shift2) % 13
                    new_char = chr((ord(char) - ord('a') - shift) % 13 + ord('a'))
                else:
                    shift = (shift1 + shift2) % 13
                    new_char = chr((ord(char) - ord('n') + shift) % 13 + ord('n'))

            # Decryption logic for uppercase letters
            elif char.isupper():
                if 'A' <= char <= 'M':
                    shift = shift1 % 13
                    new_char = chr((ord(char) - ord('A') + shift) % 13 + ord('A'))
                else:
                    shift = (shift2 ** 2) % 13
                    new_char = chr((ord(char) - ord('N') - shift) % 13 + ord('N'))

            # If character is not a letter, no change
            else:
                new_char = char

            decrypted_file.write(new_char)

    print(f"Decryption successfull")

# ///////////  VERIFICATION FUNCTION ///////////
def verification():
    with open("raw_text.txt", "r", encoding="utf-8") as raw_file, \
        open("decrypted_text.txt", "r", encoding="utf-8") as decrypted_file:

        if raw_file.read() == decrypted_file.read():
            print(f"Verification successfull")
        else:
            print(f"Verification failed")

# ///////////  MAIN FUNCTION ///////////
def main():
    if not os.path.exists("raw_text.txt"):
        print("File not found for processing")
        return
    shift1 = int(input("Enter value for shift1: "))
    shift2 = int(input("Enter value for shift2: "))

    encryption(shift1, shift2)
    decryption(shift1, shift2)
    verification()

main()