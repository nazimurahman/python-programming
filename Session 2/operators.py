# ---------- Arithmetic Operators ----------
a = 10           # integer
b = 3            # integer

# Addition: adds two numbers
sum_result = a + b               # 10 + 3 = 13
print("Addition:", sum_result)

# Subtraction: subtracts second from first
diff_result = a - b              # 10 - 3 = 7
print("Subtraction:", diff_result)

# Multiplication: multiplies two numbers
mul_result = a * b               # 10 * 3 = 30
print("Multiplication:", mul_result)

# Division: always returns float (even if evenly divisible)
div_result = a / b               # 10 / 3 = 3.3333333333333335
print("Division:", div_result)

# Floor division: integer division (floor for positives)
floor_result = a // b            # 10 // 3 = 3
print("Floor Division:", floor_result)

# Modulus: remainder of division
mod_result = a % b               # 10 % 3 = 1
print("Modulus:", mod_result)

# Exponentiation: power
exp_result = a ** b              # 10 ** 3 = 1000
print("Exponentiation:", exp_result)

# Unary plus/minus: show sign operation
pos = +a                         # +10 = 10
neg = -b                         # -3 = -3
print("Unary +:", pos, "Unary -:", neg)

# Real-life arithmetic example: splitting bill
total_bill = 250.75
people = 4
per_person = total_bill / people  # division to split cost
print("Per person bill:", per_person)

# ---------- Comparison (Relational) Operators ----------
x = 5
y = 10

# Equal: checks value equality
is_equal = (x == y)              # False
print("Equal:", is_equal)

# Not equal: checks inequality
is_not_equal = (x != y)          # True
print("Not equal:", is_not_equal)

# Greater than
is_greater = (x > y)             # False
print("Greater than:", is_greater)

# Less than
is_less = (x < y)                # True
print("Less than:", is_less)

# Greater than or equal
is_greater_equal = (x >= y)      # False
print("Greater or equal:", is_greater_equal)

# Less than or equal
is_less_equal = (x <= y)         # True
print("Less or equal:", is_less_equal)

# Chained comparisons: readable multi-part comparison
num = 7
in_range = 1 < num <= 10         # True, equivalent to (1 < num) and (num <= 10)
print("Chained comparison (1 < num <= 10):", in_range)

# Real-life comparison example: eligibility
age = 18
can_vote = age >= 18             # True if age is at least 18
print("Can vote:", can_vote)

# ---------- Logical Operators ----------
is_raining = True
has_umbrella = False

# and: True only if both operands are True
go_outside = (not is_raining) and has_umbrella   # (False) and False -> False
print("AND operator (go_outside):", go_outside)

# or: True if at least one operand is True
stay_dry = is_raining or has_umbrella           # True or False -> True
print("OR operator (stay_dry):", stay_dry)

# not: negates boolean
should_stay_home = not is_raining               # not True -> False
print("NOT operator (should_stay_home):", should_stay_home)

# Combining logicals: nested conditions (real-life driving example)
age = 25
has_license = True
is_sober = True
can_drive = (age >= 18) and has_license and is_sober  # True if all three True
print("Can drive:", can_drive)

# Short-circuit behavior demonstration
def expensive_check():
    print("expensive_check called")
    return True

# 'and' short-circuits on first False, 'or' short-circuits on first True
print("Short-circuit and:", False and expensive_check())  # expensive_check not called
print("Short-circuit or:", True or expensive_check())     # expensive_check not called

# ---------- Assignment Operators ----------
num = 10
print("Initial:", num)        # 10

# +=
num += 5                      # num = num + 5 -> 15
print("After +=:", num)       # 15

# -=
num -= 3                      # num = num - 3 -> 12
print("After -=:", num)       # 12

# *=
num *= 2                      # num = num * 2 -> 24
print("After *=:", num)       # 24

# /= results in float
num /= 4                      # num = num / 4 -> 6.0
print("After /=:", num)       # 6.0

# Convert to int for floor assignment demonstration
num = int(num)                # 6
num //= 2                     # num = num // 2 -> 3
print("After //=:", num)      # 3

# %= modulus assignment
num %= 3                      # num = num % 3 -> 0
print("After %=: ", num)      # 0

# Real-life use: incrementing counters
visitors = 0
visitors += 1                 # new visitor arrives
print("Visitors:", visitors)

# ---------- Bitwise Operators ----------
a = 5   # binary 0b0101
b = 3   # binary 0b0011

# &: bitwise and
bitwise_and = a & b           # 0b0101 & 0b0011 = 0b0001 -> 1
print("Bitwise AND:", bitwise_and)

# |: bitwise or
bitwise_or = a | b            # 0b0101 | 0b0011 = 0b0111 -> 7
print("Bitwise OR:", bitwise_or)

# ^: bitwise xor
bitwise_xor = a ^ b           # 0b0101 ^ 0b0011 = 0b0110 -> 6
print("Bitwise XOR:", bitwise_xor)

# ~: bitwise not (two's complement)
bitwise_not = ~a              # ~5 -> -6 (because of two's complement)
print("Bitwise NOT:", bitwise_not)

# <<: left shift (multiply by powers of two)
left_shift = a << 1           # 0b0101 << 1 = 0b1010 -> 10
print("Left Shift:", left_shift)

# >>: right shift (integer division by powers of two)
right_shift = a >> 1          # 0b0101 >> 1 = 0b0010 -> 2
print("Right Shift:", right_shift)

# Real-life bitwise example: using bit flags
READ = 0b100   # 4
WRITE = 0b010  # 2
EXEC = 0b001   # 1
perms = READ | EXEC            # give read and exec permissions -> 0b101 (5)
print("Permissions value:", perms)
has_write = bool(perms & WRITE)  # check write permission -> False
print("Has write permission:", has_write)

# ---------- Identity Operators ----------
list1 = [1, 2, 3]
list2 = [1, 2, 3]   # distinct object with same content
list3 = list1       # reference to same object as list1

# is: True if same object (same identity)
is_same = (list1 is list3)
print("is operator (same obj):", is_same)

# is with different object but same content -> False
is_different = (list1 is list2)
print("is operator (different objs):", is_different)

# is not: True if different objects
is_not_same = (list1 is not list2)
print("is not operator (list1 is not list2):", is_not_same)

# Comparing with None: use 'is' for identity
value = None
is_none = (value is None)
print("Check None:", is_none)

# ---------- Membership Operators ----------
fruits = ['apple', 'banana', 'orange', 'grape']
text = "Hello World"

# in: membership in sequence
has_apple = 'apple' in fruits
print("'apple' in fruits:", has_apple)

has_pear = 'pear' in fruits
print("'pear' in fruits:", has_pear)

# membership in string
has_hello = 'Hello' in text
print("'Hello' in text:", has_hello)

# not in: testing absence
not_in_list = 'mango' not in fruits
print("'mango' not in fruits:", not_in_list)

# dictionaries: 'in' checks keys by default
person = {'name': 'John', 'age': 30, 'city': 'NYC'}
has_name_key = 'name' in person           # True
print("'name' in person:", has_name_key)
has_john_value = 'John' in person.values()  # True
print("'John' in person.values():", has_john_value)

# ---------- Ternary (Conditional) Operator ----------
age = 18
status = "Adult" if age >= 18 else "Minor"  # short if-else expression
print("Status:", status)

# nested ternary (avoid for complex logic; prefer if-elif-else)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print("Grade:", grade)

# Real-life example: greeting by login state
is_logged_in = True
message = "Welcome back!" if is_logged_in else "Please login"
print("Message:", message)

# ---------- Operator Precedence ----------
result = 10 + 5 * 2 - 3 ** 2 / 2
# evaluation order: **, *, /, +, -
print("Result with normal precedence:", result)

# use parentheses to override precedence
result_with_parentheses = (10 + 5) * 2 - (3 ** 2 / 2)
print("Result with parentheses:", result_with_parentheses)

# show precedence list in brief
precedence_list = [
    "()", "**", "*, /, //, %", "+, -",
    "<<, >>", "&", "^", "|",
    "<, <=, >, >=, !=, ==", "not", "and", "or"
]
print("Operator precedence (highest->lowest):", precedence_list)

# ---------- Comprehensive Conditional Examples ----------
def calculate_bonus(salary, years_experience, performance_rating, remote=False):
    """
    Calculate employee bonus based on multiple factors:
    - qualifies if years_experience >= 3 and performance_rating >= 7
    - base bonus = 10% of salary
    - extra: 50% extra if rating >=9, 25% if rating >=8
    - remote employees receive 5% reduction in bonus (example business rule)
    """
    # qualification check (comparison + logical)
    qualifies = (years_experience >= 3) and (performance_rating >= 7)

    if not qualifies:
        # employee does not qualify
        return 0.0

    # base bonus (arithmetic)
    base_bonus = salary * 0.10

    # nested conditional for extra bonus
    if performance_rating >= 9:
        extra_bonus = base_bonus * 0.50
    elif performance_rating >= 8:
        extra_bonus = base_bonus * 0.25
    else:
        extra_bonus = 0.0

    # apply remote reduction using ternary operator
    reduction = 0.05 if remote else 0.0
    total_bonus = (base_bonus + extra_bonus) * (1 - reduction)

    # ensure non-negative and return float
    return float(max(total_bonus, 0.0))

# test cases for calculate_bonus covering multiple branches
employees = [
    {"salary": 50000, "years": 5, "rating": 8, "remote": False},  # qualifies, extra 25%
    {"salary": 40000, "years": 2, "rating": 9, "remote": False},  # not qualify (experience)
    {"salary": 60000, "years": 10, "rating": 9, "remote": True},  # qualifies, extra 50%, remote reduction
    {"salary": 30000, "years": 4, "rating": 7, "remote": False},  # qualifies, no extra
]

for e in employees:
    bonus = calculate_bonus(e["salary"], e["years"], e["rating"], e["remote"])
    print(f"Employee (salary={e['salary']}, years={e['years']}, rating={e['rating']}, remote={e['remote']}) -> Bonus: ${bonus:,.2f}")

# ---------- Multiple operators in one expression ----------
age = 25
salary = 60000
employee_status = "Senior" if (age >= 30 and salary > 50000) else "Junior"
print("Employee Status:", employee_status)

# ---------- Edge cases and safety ----------
# Avoid dividing by zero: check before division
def safe_divide(x, y):
    return x / y if y != 0 else float('inf')   # return infinity for division-by-zero case

print("Safe divide 10/0:", safe_divide(10, 0))

# Use 'is' for None checks and '==' for value equality:
a = None
print("a is None:", a is None)