import random
import os
import time
import nltk
import logging
import requests

# Suppress NLTK logging
logging.getLogger('nltk').setLevel(logging.ERROR)

# Download words corpus (only required on first run)
nltk.download('words', quiet=True)

# Load the list of words from NLTK's words corpus
word_list = nltk.corpus.words.words()

def print_border(title):
    print(f"+{'-' * (len(title) + 2)}+\n| {title} |\n+{'-' * (len(title) + 2)}+")

def read_dictionary_file(url):
    """Read words from a formatted dictionary file."""
    response = requests.get(url)
    if response.status_code == 200:
        words = [line.strip().split('. ', 1)[-1] for line in response.text.splitlines() if line.strip()]
        return words
    else:
        print("Error: Unable to load dictionary file from URL.")
        return []

def load_complex_words():
    """Load complex words into the word_list."""
    global word_list
    try:
        with open("complex_words.txt", "r") as file:
            word_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: complex_words.txt file not found.")
        word_list = []

def generate_random_words(count, mode):
    """Generate random words based on the selected mode."""
    random_words = []

    if mode == "complex":
        count = min(max(1, count), 1000)

        if len(word_list) >= count:
            random_words = random.sample(word_list, count)

    elif mode == "dictionary":
        dictionary_url = "https://raw.githubusercontent.com/100101011110101101101110110000000000010/Python-Files/refs/heads/main/Dictionary.txt"
        dictionary_words = read_dictionary_file(dictionary_url)
        count = min(max(1, count), len(dictionary_words))
        if len(dictionary_words) >= count:
            random_words = random.sample(dictionary_words, count)

    if not random_words:
        print("No words generated. Please try again.")
    return random_words

def update_generated_words_file(generated_words, file_name="Generated Words.txt"):
    """Update the file with new generated words, keeping existing content and updating line numbers."""
    existing_lines = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            existing_lines = f.readlines()

    updated_content = []
    max_index = len(existing_lines)

    # Add existing lines while preserving their content
    for line in existing_lines:
        updated_content.append(line)

    # Update the numbering for new words
    for i, word in enumerate(generated_words, max_index + 1):
        updated_content.append(f"{i}. {word}\n")

    # Write the updated content back to the file
    with open(file_name, "w") as f:
        f.writelines(updated_content)

def get_input_with_options(prompt, options):
    """Get input from the user with options."""
    print_border(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")
    while True:
        try:
            choice = int(input("Enter choice: ")) - 1
            if 0 <= choice < len(options):
                return options[choice]
        except ValueError:
            pass
        print("Invalid input. Please try again.")

def get_integer_input(prompt, min_value, max_value):
    """Get an integer input from the user within a specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
        except ValueError:
            pass
        print(f"Invalid input. Enter a number between {min_value} and {max_value}.")

def get_yes_or_no(prompt):
    """Get a yes or no response from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

def generate_words():
    modes = ["Complex", "Dictionary"]

    while True:
        print_border("Word Generator")
        mode = get_input_with_options("Select word type:", modes).lower()
        count = get_integer_input("Input the desired amount of words (1-1000): ", 1, 1000)

        generated_words = generate_random_words(count, mode)

        if not generated_words:
            print("No words generated. Please try again.")
            time.sleep(0.5)
            continue
        
        for i, word in enumerate(generated_words, 1):
            print(f"{i}. {word}")

        # Get the current directory and create the file path
        current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
        file_name = os.path.join(current_directory, "Generated Words.txt")

        if get_yes_or_no(f"Do you wish to write these {len(generated_words)} words to '{file_name}'? (y/n): "):
            update_generated_words_file(generated_words, file_name)

        if not get_yes_or_no("Generate more words? (y/n): "):
            break

if __name__ == "__main__":
    generate_words()
    input("Press ENTER to exit.")
