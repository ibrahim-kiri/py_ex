# Check palindrome number

def check_palindrome_num(number):
    
    original_number = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number //= 10

    return original_number == reversed_number

#Example usage:
print(check_palindrome_num(121))
print(check_palindrome_num(123))
