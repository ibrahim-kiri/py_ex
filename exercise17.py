# Generate Fibonacci series up to 15 terms

def fibonacci_seq():

    # First two numbers
    first_num = 0
    second_num = 1

    print("Fibonacci sequence:")

    # Run loop 15 times
    for i in range(15):

        # Print next number of a series
        print(first_num, end=" ")

        # Add last two numbers to get next number
        res = first_num + second_num

        # Update values
        first_num = second_num
        second_num = res

num = fibonacci_seq()
