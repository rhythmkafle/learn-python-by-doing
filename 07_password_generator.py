import random
import string

def menu():
    length = int(input("Enter the length of the password: "))
    upcase = input("Include Uppercase letters?(Y/N): ")    
    lwcase = input("Include Lowercase letters?(Y/N): ")    
    symbols = input("Include Symbols?(Y/N): ")    
    numbers = input("Include Numbers?(Y/N): ")    
    return (length, upcase.lower()=='y', lwcase.lower()=='y',symbols.lower()=='y',numbers.lower()=='y')

def generate_pass(length,upcase,lwcase,symbols,numbers):
    characters = ""
    if upcase:
        characters += string.ascii_uppercase
    if lwcase:
        characters += string.ascii_lowercase
    if symbols:
        characters += string.punctuation
    if numbers:
        characters += string.digits
    if not characters:
        return "At least one character must be selected"

    password = ''.join(random.choice(characters) for i in range(length))
    return password

length, upcase, lwcase, symbols, numbers = menu()
password = generate_pass(length, upcase, lwcase, symbols, numbers)

print("The generated password: %s" % password)