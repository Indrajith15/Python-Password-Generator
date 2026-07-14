import random
import string

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
def get_user_choices():
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    symbols = input("Include symbols? (y/n): ").lower()
    return length, uppercase, numbers, symbols

def build_character_pool(uppercase, numbers, symbols):
    characters = string.ascii_lowercase
    if uppercase == "y":
        characters += string.ascii_uppercase
    if numbers == "y":
        characters += string.digits
    if symbols == "y":
        characters += string.punctuation
    return characters

def generate_password(length, characters):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    length, uppercase, numbers, symbols = get_user_choices()
    characters = build_character_pool(uppercase, numbers, symbols)
    password = generate_password(length, characters)
    print("Generated password:", password)

if __name__ == "__main__":
    main()