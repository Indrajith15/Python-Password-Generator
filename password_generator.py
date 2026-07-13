import random
import string

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

characters = string.ascii_lowercase

uppercase = input("Include uppercase letters? (y/n): ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include symbols? (y/n): ").lower()

if uppercase == "y":
    characters += string.ascii_uppercase

if numbers == "y":
    characters += string.digits

if symbols == "y":
    characters += string.punctuation

length = int(input("Enter the length of the password: "))
password= ""
for i in range(length):
    password+=random.choice(characters)

print(password)

