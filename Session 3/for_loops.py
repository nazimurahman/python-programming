# Example script demonstrating for loops, conditionals, and common operators.
# Each line contains inline comments explaining keywords, variables, and operators.

# ---------- FOR LOOPS ----------

# List iteration: 'for' starts a loop, 'fruit' is loop variable that receives each element.
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:                # iterate over each element in the list 'fruits'
    print(fruit)                     # print current element

print()                              # blank line for readability

# range() usage: generate sequence of integers
for i in range(5):                   # range(5) -> 0,1,2,3,4; 'i' gets each integer
    print(f"Number: {i}")            # formatted output showing 'i'

print()

for i in range(2, 10, 2):            # start=2, stop=10 (exclusive), step=2
    print(f"Even number: {i}")       # prints even numbers 2,4,6,8

print()

# String iteration: iterate characters in a string
word = "Python"
for letter in word:                  # 'letter' receives each character
    print(f"Character: {letter}")

print()

# Dictionary iteration
person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:                   # default: iterates keys
    print(f"Key: {key}")

print()

for key, value in person.items():    # .items() returns (key, value) tuples
    print(f"{key}: {value}")

print()

# enumerate(): get index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):           # index starts at 0 by default
    print(f"Index {index}: {color}")

print()

for index, color in enumerate(colors, start=1):  # start=1 changes first index
    print(f"Position {index}: {color}")

print()

# Nested for loops: iterate a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:                   # outer loop: each 'row' is a list
    for element in row:              # inner loop: each 'element' in the current row
        print(element, end=" ")      # print elements on same line separated by space
    print()                          # newline after finishing a row

print()

# ---------- CONDITIONAL STATEMENTS ----------

# We'll show:
# - simple if
# - if-else
# - if-elif-else (multiple branches)
# - nested if
# - compound conditionals using logical operators (and, or, not)
# - membership and identity checks (in, is)
# - comparison operators (>, <, >=, <=, ==, !=)

# Example variables for realistic scenarios
temperature_c = 22                   # current temperature in Celsius
is_raining = False                   # boolean flag indicating rain
wind_speed_kmh = 15                  # wind speed in km/h
user_age = 20                        # user's age
balance = 150.0                      # bank account balance in currency units
pin_entered = "1234"                 # PIN string entered by user
correct_pin = "1234"                 # correct PIN

# Simple if: check a single condition
if temperature_c > 30:               # '>' compares temperature; True if temperature > 30
    print("It's hot today.")         # executed only when condition is True

# if-else: choose between two paths
if is_raining:                       # truthiness check of boolean variable
    print("Take an umbrella.")       # executed when is_raining is True
else:
    print("No umbrella needed.")     # executed when is_raining is False

# if-elif-else: multiple mutually exclusive branches
if wind_speed_kmh >= 100:            # checks severe wind
    print("Danger: storm force winds.") 
elif wind_speed_kmh >= 50:           # checks high wind
    print("High winds; secure loose objects.")
elif wind_speed_kmh >= 20:           # moderate wind
    print("Breezy day.")
else:
    print("Calm winds.")             # fallback when none of above are True

# Nested if: compound real-life decision (age + balance)
if user_age >= 18:                   # check legal adult (>= compares integers)
    # nested check for account balance
    if balance >= 100:               # ensures sufficient funds
        print("Eligible for premium service.")
    else:
        print("Adult but insufficient balance for premium service.")
else:
    print("Not eligible because underage.")

# Logical operators: and, or, not
# and: True only if both operands True
if user_age >= 18 and balance >= 50:
    print("Can rent a car (age and balance conditions met).")

# or: True if at least one operand True
if is_raining or wind_speed_kmh > 30:
    print("Bad weather advisory.")  # if raining OR very windy

# not: negation
if not is_raining:                   # True when is_raining is False
    print("Dry weather — good for walking.")

# Membership operator 'in' and 'not in'
allowed_users = ["alice", "bob", "nazim"]
username = "nazim"
if username in allowed_users:        # checks if 'username' exists in list
    print("User is allowed.")
else:
    print("Access denied.")

# Identity operator 'is' (checks object identity) vs equality '=='
a = [1, 2, 3]
b = [1, 2, 3]
c = a                                # c references the same object as a
if a == b:                           # equality: compares values -> True
    print("a and b have equal contents.")
if a is b:                           # identity: different objects -> usually False
    print("a and b are the same object (unlikely here).")
if a is c:                           # True because c references a
    print("a and c are the same object.")

# Comparison operators: demonstration with pin check
if pin_entered == correct_pin:       # '==' checks value equality
    print("PIN correct.")
else:
    print("PIN incorrect.")

if pin_entered != correct_pin:       # '!=' checks inequality
    print("Access blocked due to wrong PIN.")

# Combine comparisons with chained form (Python supports chaining)
x = 10
if 0 < x < 20:                       # chained comparisons: equivalent to 0 < x and x < 20
    print("x is between 0 and 20 (exclusive).")

# Ternary conditional expression for inline selection
message = "adult" if user_age >= 18 else "minor"   # assigns based on condition
print(f"User is an {message}.")

# ---------- REAL-LIFE OPERATOR USE CASES (small demos) ----------

# Arithmetic operators: +, -, *, /, //, %, **
price = 99.99
tax_rate = 0.13
total_price = price + price * tax_rate         # '+' and '*' used to compute total
discounted = price * 0.9                       # apply 10% discount
pieces = 5
unit_price = price / pieces                    # '/' gives float division
whole_pieces = 17 // 5                         # '//' floor division -> 3
remainder = 17 % 5                             # '%' modulus -> 2
power = 2 ** 3                                 # '**' exponentiation -> 8

print(f"Total price: {total_price:.2f}, discounted: {discounted:.2f}")
print(f"Unit price: {unit_price:.2f}, quotient: {whole_pieces}, remainder: {remainder}, power: {power}")

# Bitwise operators example (rare in daily app code, but used for flags)
flags = 0b0010                                # binary literal, bit 1 set
MASK = 0b0001
if flags & MASK:                              # '&' bitwise AND checks that specific bit
    print("Mask bit is set.")
else:
    print("Mask bit not set.")

# Short-circuit behavior example: and/or stop evaluation early
def expensive_check():
    print("Running expensive check...")
    return True

# in 'and', if left operand False, right operand not evaluated
if False and expensive_check():
    print("Won't print; expensive_check not called due to short-circuit.")

# in 'or', if left operand True, right operand not evaluated
if True or expensive_check():
    print("expensive_check not called because left side True.")

# ---------- END OF SCRIPT ----------