# Solution 1

def is_palindrome(number):

    # Handle negative numbers (they are typically not palindrones)
    if number < 0:
        return False

    # Convert the number to a string
    original_string = str(number)

    # Reverse the string using slicing
    reversed_string = original_string[::-1]

    # Compare the original and reversed strings
    if original_string == reversed_string:
        return True
    else:
        return False

# Test case
print(is_palindrome(121))
print(is_palindrome(123))


# Solution 2

def palindrome(number):
    print("original number", number)
    original_num = number

    # Reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

