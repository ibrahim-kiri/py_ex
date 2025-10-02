# Function that takes two numbers as parameter
def multi_or_sum(number1, number2):

    # calculate the product of two numbers
    product = number1 * number2

    # check if product is less than 1000
    if product <= 1000:
        return product
    else:
        # if product is gt 1000 calculate the sum
        return number1 + number2

# first condition
res = multi_or_sum(20, 30)
print("The result of multiplication is: ", res)

# second condition
res = multi_or_sum(40, 30)
print("The result of addition is: ", res)

