import os

def encryption(shift1, shift2):
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