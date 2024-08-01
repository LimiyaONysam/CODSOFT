
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    num_passwords = int(input("How many passwords to generate? "))

    for i in range(num_passwords):
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        if password:
            print(f"Generated Password {i+1}: {password}")

if __name__ == "__main__":
    main()
