# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Set N
n = 20
primes = [] # List to store all prime numbers
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

# Printing all prime numbers
print(f'All prime numbers from 1 to {n}: {primes}')

# Printing alternate prime numbers from the list
print(f'Alternate prime numbers from 1 to {n}:')

for i in range(0, len(primes), 2):
    print(primes[i], end=" ")


