# Capitalize the first letter of each word in a string

def capitalize_words(text):

    # Split the string into a list of words
    words = text.split()

    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words into a string
    return " ".join(capitalized_words)

# Get input from the user
str1 = "django.com is for python lovers"

capitalized_string = capitalize_words(str1)
print("Capitalized string:", capitalized_string)

