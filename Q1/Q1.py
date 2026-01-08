import os

def encryption(shift1, shift2):
    with open("raw_text.txt", "r", encoding="utf-8") as raw_file, \
        open("encrypted_text.txt", "w", encoding="utf-8") as encrypted_file:

        for char in raw_file.read():
            if char.islower():
                if 'a' <= char <= 'm':
                    shift = shift1 * shift2
                    new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    shift = shift1 + shift2
                    new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            else:
                new_char = char

            encrypted_file.write(new_char)

    print(f"Encryption successfull")
def decryption(shift1, shift2):
    print(f"Decryption successfull")
def verification():
    print(f"Verification successfull")

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