# Nested Loops (Combining for and while)

# for inside while
# Example 1: While loop containing for loop
row = 1

while row <= 3:  # Outer while loop
    print(f"Row {row}: ", end="")
    
    for col in range(1, 4):  # Inner for loop
        print(f"{col}", end=" ")
    
    print()  # New line
    row += 1  # Increment row

# Output:
# Row 1: 1 2 3
# Row 2: 1 2 3
# Row 3: 1 2 3


# while inside for

# Example 2: For loop containing while loop
for i in range(1, 4):  # Outer for loop
    print(f"Multiplication table for {i}: ")
    
    j = 1
    while j <= 10:  # Inner while loop
        print(f"{i} x {j} = {i * j}")
        j += 1  # Increment counter
    
    print()  # Empty line for readability


# Loop Control Statements:

# break Statement
# break - exits the loop immediately
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        print("Found 5! Breaking the loop.")
        break  # Exits the loop completely when num == 5
    print(f"Checking: {num}")

# Output:
# Checking: 1
# Checking: 2
# Checking: 3
# Checking: 4
# Found 5! Breaking the loop.


# continue Statement
# continue - skips current iteration
for num in range(1, 11):
    if num % 2 == 0:  # If even number
        continue  # Skip the rest of the loop for this iteration
    print(f"Odd number: {num}")

# Output: 1, 3, 5, 7, 9 (only odd numbers)

# pass Statement
# pass - does nothing (placeholder)
for i in range(5):
    if i == 2:
        pass  # Placeholder - does nothing, useful for future implementation
    else:
        print(f"Number: {i}")

# Output: 0, 1, 3, 4 (skips 2 because pass does nothing)



# else with Loops

# else clause with loops - executes when loop completes normally
# The else block executes only if the loop wasn't terminated by break

# Case 1: Loop completes normally
for i in range(3):
    print(f"Attempt {i+1}")
else:
    print("Loop completed without break!")  # This will execute

print("\n")

# Case 2: Loop terminated by break
for i in range(5):
    if i == 3:
        print("Breaking at 3!")
        break  # Breaks the loop
    print(f"i = {i}")
else:
    print("This won't execute because of break")  # Won't execute


# List Comprehensions (Shorthand for loops)

# Creating a list using comprehension
# Traditional for loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"Traditional: {squares}")

# List comprehension (more Pythonic)
squares_comprehension = [x ** 2 for x in range(1, 6)]
print(f"Comprehension: {squares_comprehension}")

# With condition
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Dictionary comprehension
# Create dictionary with squares of numbers 1-5
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Dictionary comprehension: {squares_dict}")

# With condition
even_squares_dict = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares dict: {even_squares_dict}")


# zip() Function for Parallel Iteration
#  Using zip() to iterate multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Iterate over all three lists together
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Output:
# Alice is 25 years old and lives in NYC
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in Chicago

# itertools Module
# Using itertools for advanced looping
import itertools

# Infinite counter
counter = itertools.count(start=1, step=2)  # Starts at 1, increments by 2
print("First 5 numbers from counter:")
for i in range(5):
    print(next(counter), end=" ")  # Outputs: 1 3 5 7 9

print("\n")

# Cycle through a sequence
colors = ["red", "green", "blue"]
color_cycle = itertools.cycle(colors)  # Infinite cycle
print("First 6 colors from cycle:")
for i in range(6):
    print(next(color_cycle), end=" ")  # Outputs: red green blue red green blue


# Performance Comparison: -> Different Loop Types    

import time

# Example: Comparing loop performance
def performance_comparison():
    # Method 1: Traditional for loop
    start = time.time()
    result1 = []
    for i in range(1000000):
        result1.append(i ** 2)
    time1 = time.time() - start
    
    # Method 2: List comprehension
    start = time.time()
    result2 = [i ** 2 for i in range(1000000)]
    time2 = time.time() - start
    
    # Method 3: map() function
    start = time.time()
    result3 = list(map(lambda x: x ** 2, range(1000000)))
    time3 = time.time() - start
    
    print(f"Traditional loop: {time1:.4f} seconds")
    print(f"List comprehension: {time2:.4f} seconds")
    print(f"map() function: {time3:.4f} seconds")

# Uncomment to run (takes a moment)
# performance_comparison()

# Note: List comprehension is generally fastest for simple operations


# Infinite loop (DANGER!)
# while True:
#     print("This will run forever!")  # Infinite loop - never do this without a break

# Proper infinite loop with break condition
count = 0
while True:
    print(f"Loop iteration: {count}")
    count += 1
    if count >= 5:  # Break condition
        break  # Prevents infinite loop

# Example 2: Off-by-one error causing infinite loop
# count = 0
# while count < 5:
#     print(count)  # Forgot to increment count - infinite loop!

# Correct version:
count = 0
while count < 5:
    print(f"Correct count: {count}")
    count += 1  # Always remember to increment!



# Common Loop Patterns and Best Practices

# Pattern 1: Iterating with index
fruits = ["apple", "banana", "cherry"]

# Use enumerate() instead of range(len())
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# Pattern 2: Reversing a sequence
for item in reversed(fruits):
    print(f"Reversed: {item}")

# Pattern 3: Sorted iteration
for item in sorted(fruits):
    print(f"Sorted: {item}")

# Pattern 4: Iterating over two lists simultaneously
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Pattern 5: Using any() and all() with loops
numbers = [1, 2, 3, 4, 5]

# Check if any number is even
has_even = any(num % 2 == 0 for num in numbers)
print(f"Has even number: {has_even}")  # True

# Check if all numbers are positive
all_positive = all(num > 0 for num in numbers)
print(f"All numbers positive: {all_positive}")  # True
