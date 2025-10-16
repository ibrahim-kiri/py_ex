# Get an int value of base raises to the power of exponent

#example 1

def exponent(base, exp):

    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)


#example 2

def exponent_two(base, exp):
    num = exp
    result = 1
    while num > 0:
        print("Before multiplying: num =", num, ", result =", result)
        result = result * base
        print("After multiplying: result =", result)

        num = num - 1
        print("After subtracting 1: num =", num)
        print("-----")

    print(base, "raises to the power of", exp, "is:", result)

exponent_two(5, 4)
