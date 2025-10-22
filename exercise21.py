# Check if a user-entered string contains any digits using a for loop

def contains_digits(text):

    for char in text:
        if '0' <= char <= '9':
            return True # Found a digit, so return True immediately  
    return False # No digit found after checking all characters

# Get input from the user
user_string = input("Enter a string: ")

if contains_digits(user_string):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")

