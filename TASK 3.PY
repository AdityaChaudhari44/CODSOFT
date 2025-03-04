import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters to create the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Main function
def password_generator():
    print("Welcome to the Password Generator!")

    # Prompt the user to enter the desired password length
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 6:  # Setting a minimum length for stronger passwords
                print("Password length should be at least 6 characters for better security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for the length.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Your generated password is: {password}")

# Run the password generator
password_generator()
