# ---------- IMPORTS ----------
import itertools           # provides advanced iterators (count, cycle, etc.)
import time                # used for simple performance timing demos

# ---------- NESTED LOOPS (for inside while) ----------
row = 1                     # initialize row counter

while row <= 3:              # while: loop while condition (row <= 3) is True
    print(f"Row {row}:", end=" ")  # print row label; end=" " prevents newline
    for col in range(1, 4):  # for: iterate over iterable from 1 to 3 (range stop exclusive)
        print(col, end=" ")  # print each column value on same line
    print()                  # newline after inner loop completes
    row += 1                 # increment row (avoid infinite loop)

# ---------- NESTED LOOPS (while inside for) ----------
for i in range(1, 4):       # outer for: i takes values 1,2,3
    print(f"Multiplication table for {i}:")  # header for table
    j = 1                   # initialize inner counter
    while j <= 10:          # inner while: loop j from 1 to 10 inclusive
        print(f"{i} x {j} = {i * j}")  # '*' multiplies numbers
        j += 1              # increment j to eventually stop the while loop
    print()                 # blank line for readability

# ---------- LOOP CONTROL: break, continue, pass ----------
numbers = list(range(1, 11))  # list of numbers 1..10

for num in numbers:
    if num == 5:             # comparison operator '==' checks equality
        print("Found 5! Breaking the loop.")
        break                # break: exit loop immediately
    print(f"Checking: {num}")

# continue: skip remainder of current iteration
for num in range(1, 11):
    if num % 2 == 0:         # modulus '%' remainder; even numbers have remainder 0
        continue             # continue: skip printing even numbers
    print(f"Odd number: {num}")

# pass: placeholder that does nothing (useful in stubs)
for i in range(5):
    if i == 2:
        pass                 # pass does nothing; keeps syntax valid
    else:
        print(f"Number: {i}")

# ---------- else with loops ----------
for i in range(3):          # loop runs through all values 0,1,2
    print(f"Attempt {i+1}")
else:                       # else runs only if loop wasn't terminated by break
    print("Loop completed without break!")

for i in range(5):
    if i == 3:
        print("Breaking at 3!")
        break               # breaking prevents the else clause below from running
    print(f"i = {i}")
else:
    print("This won't execute because of break")

# ---------- LIST / DICT COMPREHENSIONS ----------
# Traditional list building
squares = []
for x in range(1, 6):
    squares.append(x ** 2)  # '**' exponentiation
print(f"Traditional: {squares}")

# List comprehension (more concise, often faster)
squares_comp = [x ** 2 for x in range(1, 6)]
print(f"Comprehension: {squares_comp}")

# Comprehension with condition (only even x)
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Dictionary comprehension: key -> squared value
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Dictionary comprehension: {squares_dict}")

# Conditional dict comprehension (only even keys)
even_squares_dict = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares dict: {even_squares_dict}")

# ---------- zip() FOR PARALLEL ITERATION ----------
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]
for name, age, city in zip(names, ages, cities):  # zip pairs elements by index
    print(f"{name} is {age} years old and lives in {city}")

# ---------- ITERTOOLS EXAMPLES ----------
counter = itertools.count(start=1, step=2)  # infinite counter 1,3,5,...
print("First 5 numbers from counter:", end=" ")
for _ in range(5):
    print(next(counter), end=" ")            # next() gets next value from iterator
print()

color_cycle = itertools.cycle(["red", "green", "blue"])  # infinite cycle through list
print("First 6 colors from cycle:", end=" ")
for _ in range(6):
    print(next(color_cycle), end=" ")
print()

# ---------- PERFORMANCE NOTE (simple timing demo) ----------
def performance_comparison(n=100_000):
    # measure three methods to build list of squares (timings approximate)
    start = time.time()
    result1 = []
    for i in range(n):
        result1.append(i ** 2)
    time1 = time.time() - start

    start = time.time()
    result2 = [i ** 2 for i in range(n)]
    time2 = time.time() - start

    start = time.time()
    result3 = list(map(lambda x: x ** 2, range(n)))
    time3 = time.time() - start

    print(f"Traditional loop: {time1:.4f} seconds")
    print(f"List comprehension: {time2:.4f} seconds")
    print(f"map() function: {time3:.4f} seconds")

# Uncomment to run performance test (may take time)
# performance_comparison(200_000)

# ---------- SAFE INFINITE LOOP EXAMPLE ----------
count = 0
while True:                 # True creates an infinite loop unless broken
    print(f"Loop iteration: {count}")
    count += 1
    if count >= 5:          # explicit break condition to stop loop
        break

# ---------- COMMON LOOP PATTERNS & BEST PRACTICES ----------
fruits = ["apple", "banana", "cherry"]

# 1) Iterate with index using enumerate (preferred over range(len(...)))
for i, fruit in enumerate(fruits):  # enumerate yields (index, value)
    print(f"Index {i}: {fruit}")

# 2) Reverse a sequence using reversed()
for item in reversed(fruits):
    print(f"Reversed: {item}")

# 3) Sorted iteration using sorted() (doesn't modify original list)
for item in sorted(fruits):
    print(f"Sorted: {item}")

# 4) Iterate over two lists using zip()
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 5) any() and all() with generator expressions (lazy evaluation)
numbers = [1, 2, 3, 4, 5]
has_even = any(num % 2 == 0 for num in numbers)   # any: True if any element True
all_positive = all(num > 0 for num in numbers)    # all: True if all elements True
print(f"Has even number: {has_even}")
print(f"All numbers positive: {all_positive}")

# ---------- CONDITIONAL STATEMENTS: ALL COMMON CASES ----------
temperature_c = 22           # numeric variable
is_raining = False           # boolean variable
wind_speed_kmh = 15          # numeric variable
user_age = 20                # numeric variable
balance = 150.0              # numeric variable
pin_entered = "1234"         # string variable
correct_pin = "1234"         # string variable
allowed_users = ["alice", "bob", "nazim"]  # list for membership checks

# Simple if
if temperature_c > 30:       # '>' compares numeric values
    print("It's hot today.") # executed only when condition True

# if-else
if is_raining:               # truthiness check for boolean variable
    print("Take an umbrella.")
else:
    print("No umbrella needed.")

# if-elif-else (multiple mutually exclusive branches)
if wind_speed_kmh >= 100:    # check highest-priority condition first
    print("Danger: storm force winds.")
elif wind_speed_kmh >= 50:   # checked if previous condition False
    print("High winds; secure loose objects.")
elif wind_speed_kmh >= 20:
    print("Breezy day.")
else:
    print("Calm winds.")

# Nested if (compound decision)
if user_age >= 18:           # outer condition checks adulthood
    if balance >= 100:       # inner condition checks account balance
        print("Eligible for premium service.")
    else:
        print("Adult but insufficient balance for premium service.")
else:
    print("Not eligible because underage.")

# Compound logical operators: and, or, not (short-circuiting)
if user_age >= 18 and balance >= 50:  # both conditions must be True
    print("Can rent a car (age and balance conditions met).")

if is_raining or wind_speed_kmh > 30:  # either condition True is enough
    print("Bad weather advisory.")

if not is_raining:                     # negation: True when is_raining is False
    print("Dry weather — good for walking.")

# Membership (in / not in)
username = "nazim"
if username in allowed_users:          # checks membership in list
    print("User is allowed.")
else:
    print("Access denied.")

# Identity vs equality: 'is' checks object identity; '==' checks value equality
a = [1, 2, 3]
b = [1, 2, 3]
c = a
if a == b:                             # compares contents -> True
    print("a and b have equal contents.")
if a is b:                             # different objects with same contents -> likely False
    print("a and b are the same object.")
if a is c:                             # c references same object as a -> True
    print("a and c are the same object.")

# Comparison operators and chained comparisons
if pin_entered == correct_pin:         # equality check for strings
    print("PIN correct.")
else:
    print("PIN incorrect.")

if pin_entered != correct_pin:         # inequality check
    print("Access blocked due to wrong PIN.")

x = 10
if 0 < x < 20:                         # chained comparisons (0 < x and x < 20)
    print("x is between 0 and 20 (exclusive).")

# Ternary conditional expression (inline if-else)
message = "adult" if user_age >= 18 else "minor"
print(f"User is an {message}.")

# ---------- REAL-LIFE OPERATOR EXAMPLES ----------
# Arithmetic: + - * / // % **
price = 99.99
tax_rate = 0.13
total_price = price + price * tax_rate    # add and multiply to compute taxed price
discounted = price * 0.9                  # 10% discount
unit_price = price / 5                    # '/' float division
whole_pieces = 17 // 5                    # '//' floor division -> 3
remainder = 17 % 5                        # '%' modulus -> 2
power = 2 ** 3                            # '**' exponentiation -> 8
print(f"Total price: {total_price:.2f}, discounted: {discounted:.2f}")
print(f"Unit price: {unit_price:.2f}, quotient: {whole_pieces}, remainder: {remainder}, power: {power}")

# Bitwise operators (useful for flags, masks)
flags = 0b0010
MASK = 0b0010
if flags & MASK:                          # '&' bitwise AND tests whether MASK bit set
    print("Mask bit is set.")
else:
    print("Mask bit not set.")

# Short-circuit examples: and / or skip evaluation of right-hand side when not needed
def expensive_check():
    print("Running expensive check...")
    return True

if False and expensive_check():           # left False causes short-circuit; function not called
    print("Won't print.")
if True or expensive_check():             # left True causes short-circuit; function not called
    print("Short-circuit prevented expensive_check call.")