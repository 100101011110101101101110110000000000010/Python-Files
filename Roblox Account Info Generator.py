import random
import os

def print_border(title):
    print(f"+{'-' * (len(title) + 2)}+\n| {title} |\n+{'-' * (len(title) + 2)}+")

def generate_random_string(length, charset):
    if not charset:  # Check if the charset is empty
        raise ValueError("Charset cannot be empty.")
    return "".join(random.choice(charset) for _ in range(length))

def generate_username(mode, length):
    charsets = {
        "Numbers": "0123456789",
        "Lowercase": "abcdefghijklmnopqrstuvwxyz",
        "Uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "L & U": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "Randomize": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        "Underscore": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_",
        "Barcode": "Il",
        "Barcode Special": "IlllIIIIIll_",
        "Barcode Complex": "IlLIIIllLL_",
        "Barcode PB": "IIlIlllIllllIlllIlIl_1234567890",
        "Barcode Extreme": "Il1O0"
    }
    charset = charsets.get(mode, "")
    if not charset:
        print(f"Error: Invalid username mode '{mode}'")
        return None
    return generate_random_string(length, charset)

def generate_password(length, mode):
    charsets = {
        "Numbers": "0123456789",
        "Lowercase": "abcdefghijklmnopqrstuvwxyz",
        "Uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "Underscore": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_",
        "Special": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>/?",
        "Complex & Foreign": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>/?áüç¿¡©你我是不的他会在一这个あいうえおかきくこさすせそ口"
    }
    charset = charsets.get(mode, "")
    if not charset:
        print(f"Error: Invalid password mode '{mode}'")
        return None
    return generate_random_string(length, charset)

def get_input_with_options(prompt, options, mapping):
    print_border(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")
    while True:
        try:
            choice = int(input("Enter choice: ")) - 1
            if 0 <= choice < len(options):
                return mapping[choice]  # Return the mapped value
        except ValueError:
            pass
        print("Invalid input.")

def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
        except ValueError:
            pass
        print(f"Enter a number between {min_value} and {max_value}.")

def get_yes_or_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

def generate_usernames():
    modes_user = [
        "Numbers", "Lowercase", "Uppercase", 
        "L & U", "Randomize", "Underscore", 
        "Barcode", "Barcode Special", "Barcode Complex", 
        "Barcode PB", "Barcode Extreme"
    ]
    
    modes_pass = [
        "Numbers", "Lowercase", "Uppercase", 
        "Underscore", "Special", "Complex & Foreign"
    ]

    modes_user_display = [
        "Numbers", "Lowercase", "Uppercase", 
        "L & U (Lowercase & Uppercase)", "Randomize", "Underscore", 
        "Barcode (Recommended)", "Barcode Special", "Barcode Complex", 
        "Barcode PB", "Barcode Extreme"
    ]
    
    modes_pass_display = [
        "Numbers", "Lowercase", "Uppercase", 
        "Underscore", "Special", "Complex & Foreign (Recommended)"
    ]

    user_mapping = modes_user + ["Barcode"] * 5  # Match with display options
    pass_mapping = modes_pass + ["Complex & Foreign"]  # Match with display options

    # Specify the path for the generated file in the same directory as the script
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
    file_name = os.path.join(current_directory, "Generated Accounts.txt")

    while True:
        print_border("Generator")
        u_mode = get_input_with_options("Username Mode:", modes_user_display, user_mapping)
        u_length = get_integer_input("Username Length (3-20): ", 3, 20)
        p_mode = get_input_with_options("Password Mode:", modes_pass_display, pass_mapping)
        p_length = get_integer_input("Password Length (8-200): ", 8, 200)
        count = get_integer_input("How many? (1-1000): ", 1, 1000)

        entries = []
        for _ in range(count):
            username = generate_username(u_mode, u_length)
            password = generate_password(p_length, p_mode)
            if username and password:
                entries.append(f"{username} ---> {password}")
            else:
                print("Failed to generate username or password.")

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                existing_content = file.read()
        except FileNotFoundError:
            existing_content = ""

        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(entries) + "\n" + existing_content)

        print(f"Saved to {file_name}")

        # Display number of generated pairs
        print(f"Generated and saved {len(entries)} username-password pairs to {file_name}")

        if get_yes_or_no("Open file? (y/n): "):
            os.startfile(file_name)

        if not get_yes_or_no("Generate more? (y/n): "):
            break

if __name__ == "__main__":
    generate_usernames()
    input("Press ENTER to exit.")
