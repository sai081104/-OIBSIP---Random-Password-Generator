# Random Password Generator - Command Line Version

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on the specified criteria."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected!")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the password length: "))
        if length <= 0:
            print("Invalid length! Please enter a positive number.")
            return

        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter numeric values for length.")

if __name__ == "__main__":
    main()
