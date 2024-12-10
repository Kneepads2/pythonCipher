#Kneepads2 - Dylan - 8/25/2024

print("\nCiphering\n========================\n")

def encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) + s - 48) % 10 + 48)
        else:
            result += char

    return result

def decrypt(text):
    possible_results = []

    for i in range(26): 
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) - i - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - i - 97) % 26 + 97)
            elif char.isdigit():
                result += chr((ord(char) - i - 48) % 10 + 48)
            else:
                result += char
        possible_results.append((i, result))
    return possible_results

while True:
    action = input("1. Encode text\n2. Decode text\n3. Exit\nSelect an action: ")

    if action == '1':
        shift_range = int(input("\nHow much do you want the text to shift (1-25): "))
        if 1 <= shift_range <= 25:
            string = input("Enter a string to encrypt: ")
            print("\nText: " + string)
            print("Shift: " + str(shift_range))
            print("Cipher: " + encrypt(string, shift_range) + " \n")
        else:
            print("Invalid, choose a number between 1 and 25.\n")

    elif action == '2':
        to_decrypt = input("Enter a string to decrypt: ")
        possible_decryptions = decrypt(to_decrypt)
        print("\nPossible decryptions:")
        for shift, decrypted_text in possible_decryptions:
            print(f"Shift {shift}: {decrypted_text}")
        print()
    
    elif action == '3':
        confirm_exit = input("Are you sure you want to exit? (yes/no): ")
        if confirm_exit.lower() == 'yes' or confirm_exit.lower() == 'y':
            print("Exiting...")
            break
        else:
            print("Returning to menu...\n")
    else:
        print("Invalid choice. Please select a valid option.\n")

