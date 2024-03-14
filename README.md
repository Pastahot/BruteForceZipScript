# Brute-Force Zip File Password Cracker Script

This script is designed to perform a brute-force attack on a password-protected zip file, attempting to guess the password through systematic trial and error. It consists of two main functions, `extract_zip` and `brute_force`, leveraging the `zipfile` and `itertools.product` modules for operations.

## Import Modules

- **`zipfile`**: Used for reading and extracting zip files.
- **`itertools.product`**: Utilized to generate all possible combinations of characters for the passwords.
- **`os`**: Imported but not used in the script.

## `extract_zip` Function

### Purpose

Attempts to extract the contents of a specified zip file using a given password.

### Parameters

- `zipfilename`: The path or name of the zip file to be extracted.
- `password`: The password string to attempt for extracting the zip file.

### Process

- Opens the zip file in read mode.
- Attempts to extract all files using the provided password. If the password is correct and extraction is successful, it prints the names of the files inside the zip and reads the content of `.txt` files, printing their contents.
- Handles errors for bad zip files and incorrect passwords, returning `False` in those cases.

## `brute_force` Function

### Purpose

Performs a brute-force attack to guess the password of a zip file.

### Process

- Defines a character set to use for generating password guesses and sets a maximum password length.
- Iterates through all possible combinations of characters from the character set up to the maximum length, using each combination as a password attempt.
- Calls `extract_zip` with each password attempt. If a password successfully extracts the zip file, it prints and returns the password.
- Handles file not found and bad zip file errors.

### Execution

- The script initiates the brute-force process on a predefined zip file named `TryMe.Zip`, attempting to find its password.

This script showcases a simple but powerful approach to password guessing, useful for educational purposes to understand security and password strength.
