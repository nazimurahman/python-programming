# for Loop: -> The for loop is used for iterating over a sequence (list, tuple, string, range, dictionary, etc.)


# Basic for Loop with List
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]

# Traditional for loop to print each fruit
for fruit in fruits:  # 'fruit' is the iterator variable that takes each element
    print(fruit)      # Prints each fruit one by one

# Output:
# apple
# banana
# cherry
# date


# for Loop with range()

# range(start, stop, step) - start is inclusive, stop is exclusive
for i in range(5):           # range(5) generates 0,1,2,3,4
    print(f"Number: {i}")    # Prints 0 to 4

print("\n")  # New line for clarity

for i in range(2, 10, 2):    # Start=2, Stop=10 (exclusive), Step=2
    print(f"Even number: {i}")  # Prints 2,4,6,8


# for Loop with String

word = "Python"

for letter in word:          # Each character becomes the iterator
    print(f"Character: {letter}")  # Prints P, y, t, h, o, n



# for Loop with Dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterating over keys (default behavior)
for key in person:
    print(f"Key: {key}")  # Prints keys only


# Iterating over key-value pairs using .items()
for key, value in person.items():  # .items() returns key-value pairs as tuples
    print(f"{key}: {value}")       # Prints all key-value pairs


#  for Loop with enumerate(): -> to get index and value
colors = ["red", "green", "blue"]

# enumerate() adds a counter to the iterable
for index, color in enumerate(colors):  # index starts from 0 by default
    print(f"Index {index}: {color}")

print("\n")

# Starting index from 1
for index, color in enumerate(colors, start=1):  # start parameter changes starting index
    print(f"Position {index}: {color}")



# Nested for Loops    
# Example 6: Nested for loops (loop inside another loop)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Outer loop iterates over rows, inner loop iterates over columns
for row in matrix:           # Each row is a list
    for element in row:      # Each element in the row
        print(element, end=" ")  # Print elements in same line
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 