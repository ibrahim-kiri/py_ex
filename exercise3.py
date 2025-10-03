## Solution 1

# accept input string from a user
word = input("Enter word ")
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


## Solution 2

# accept input string from a user
word = input("Enter word ")
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
