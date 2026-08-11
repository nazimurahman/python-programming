# NOTE: Comments explain keywords, operators, and function usages.

# Section 1: Basic strings and operations
s1 = 'Hello World'                    # s1: variable assigned to single-quoted string literal
s2 = "Python Programming"             # s2: variable assigned to double-quoted string literal
s3 = '''Multi-line
string example'''                     # s3: triple-quoted string supports newlines
s4 = """Another multi-line
string"""                             # s4: another triple-quoted example

# Concatenation and repetition
greeting = "Hello" + " " + "World"    # + concatenates strings; " " is space literal
laugh = "Ha" * 3                      # * repeats string 3 times

# Indexing and slicing
text = "Hello World"
first_char = text[0]                  # [0] index operator, gets first character 'H'
last_char = text[-1]                  # [-1] negative index, last character 'd'
slice_0_5 = text[0:5]                 # [start:end] slice, end excluded -> "Hello"
slice_from6 = text[6:]                # omitted start means from 6 to end -> "World"
reverse_text = text[::-1]             # [start:stop:step] negative step reverses string
every2 = text[::2]                    # step=2 picks every second char

# Section 2: Comparison operators examples with strings
a = "apple"
b = "banana"

# Equality and inequality
eq = (a == b)                         # == compares values (lexicographic for strings)
neq = (a != b)                        # != checks not equal

# Lexicographic comparisons (<, <=, >, >=)
lt = a < b                            # True if 'apple' comes before 'banana' lexicographically
le = a <= "apple"                     # <= includes equality

# Section 3: Membership and identity with strings
cmds = ["start", "stop", "pause", "quit"]  # list of allowed commands
c = "start"
in_allowed = c in cmds                 # 'in' checks membership in sequence

# identity: 'is' compares object identity (not value equality)
s_short1 = "hi"
s_short2 = "hi"
identity_same = (s_short1 is s_short2) # small strings often interned; may be True
s_long1 = "this is a longer string that may not be interned"
s_long2 = "this is a longer string that may not be interned"
identity_diff = (s_long1 is s_long2)   # usually False; content equality still True

# Section 4: Conditional branching examples (if/elif/else)
temp = 22                             # temperature example (int)
if temp < 0:                          # 'if' starts branch; '<' comparison
    print("Freezing")                 # prints when condition True
elif temp <= 18:                      # 'elif' checked if previous False
    print("Cool")
elif temp <= 25:
    print("Comfortable")
else:
    print("Warm")

# Section 5: Logical operators with real-life examples (and, or, not)
username = "admin"
password = "s3cret"

# login allowed when username matches and password length ok
if username == "admin" and len(password) >= 6:  # 'and' requires both True
    login_ok = True
else:
    login_ok = False

# alert example using 'or' and 'not'
sensor_temp = 85
sensor_vib = 0.03
error_flag = False

if sensor_temp > 80 or sensor_vib > 0.05 or error_flag:  # 'or' any True triggers
    alert = True
else:
    alert = False

# Using 'not' to invert a condition
if not alert:                       # 'not' negates boolean value
    print("System normal")

# Section 6: Chained comparisons (clean range checks)
value = 15
in_range = 10 < value <= 20         # chained comparisons: equivalent to (10 < value) and (value <= 20)

# Section 7: Nested conditionals (practical banking example)
balance = 250.0
withdraw = 200.0

if withdraw <= 0:                   # guard against non-positive withdrawal
    print("Invalid amount")
elif withdraw > balance:            # insufficient funds
    print("Insufficient funds")
else:                               # possible withdrawal -> nested checks
    daily_limit = 1000.0
    min_balance = 10.0
    # nested: both conditions required to allow withdrawal
    if withdraw <= daily_limit and (balance - withdraw) >= min_balance:
        balance -= withdraw
        print("Withdrawal successful; new balance:", balance)
    elif withdraw > daily_limit:
        print("Denied: exceeds daily limit")
    else:
        print("Denied: would drop below minimum balance")

# Section 8: Combining string methods and conditionals (command parsing)
def process_command(cmd: str) -> str:
    """Process a text command using string ops and conditionals."""
    # strip whitespace, make lowercase for case-insensitive comparison
    token = cmd.strip().lower()      # strip() removes whitespace, lower() normalizes case
    if token == "quit":              # equality check with normalized token
        return "Exiting"
    if token in cmds:                # membership check in allowed commands list
        return f"Command accepted: {token}"
    # check prefix using startswith
    if token.startswith("say "):     # startswith checks prefix presence
        return token[4:]             # return substring after prefix
    # fallback
    return "Unknown command"

# Section 9: Safe input loop demonstrating conditionals and prevention of infinite loops
def ask_for_name():
    while True:                     # loop until explicit break
        s = input("Enter your name (or 'quit'): ").strip()
        if s.lower() == "quit":     # case-insensitive quit
            print("Goodbye")
            break                    # break exits loop
        # conditional checks showing string methods
        if not s:                   # empty string -> Falsey; not s True when empty
            print("Please type a non-empty name")
            continue                 # continue restarts loop
        if any(ch.isdigit() for ch in s):  # any() with generator checks for digits
            print("Names cannot contain numbers")
            continue
        print("Hello,", s)          # Accepted name
        break

# Section 10: Demonstrating all comparison operators in string contexts
examples = [
    ("", ""), ("a", "A"), ("abc", "abd"), ("abc", "abc"), ("abc", "abcd")
]
for left, right in examples:
    # equality/inequality, less/greater, less-or-equal, greater-or-equal
    print(f"Comparing '{left}' and '{right}':",
          left == right,             # equality
          left != right,             # inequality
          left < right,              # lexicographic less-than
          left <= right,             # less-or-equal
          left > right,              # greater-than
          left >= right)             # greater-or-equal

# Section 11: Using membership and count with conditionals
text = "Hello World, Hello Python"
if "Hello" in text:                 # substring membership check
    cnt = text.count("Hello")       # count occurrences
    if cnt > 1:                     # conditional on count
        print("Repeated greeting found", cnt, "times")

# Section 12: Regex example combined with conditionals
import re
digits = re.findall(r'\d+', "Invoice 123, Invoice 456")  # find digits
if digits:                            # non-empty list is truthy
    for d in digits:
        # conditional numeric check after conversion
        num = int(d)
        if num > 200:
            print("Large invoice number:", num)
        else:
            print("Invoice number:", num)

# Section 13: Edge cases & safe patterns
# 1) Avoid comparing None with string using operators like '<' (will raise TypeError)
maybe_none = None
if maybe_none is None:                # identity check for None
    print("No value provided")

# 2) Use try/except for conversions that might fail
def parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None

n = parse_int("12a")
if n is None:
    print("Could not parse integer")

# 3) Be explicit with boolean checks instead of relying on truthiness when clarity matters
s = " "
if s.strip():                         # strip removes whitespace; non-empty -> truthy
    print("Contains non-whitespace")
else:
    print("Only whitespace or empty")

# Section 14: Examples showing all boolean operators in one conditional
username = "user"
role = "admin"
login_success = True

# Combined condition: proceed if logged in and (is admin or has special role) and not suspended
suspended = False
if login_success and (role == "admin" or role == "moderator") and not suspended:
    print("Access granted")
else:
    print("Access denied")

# Section 15: Function examples combining string ops and nested conditionals for realism
def classify_text(s: str) -> str:
    """Return classification using string checks and nested conditionals."""
    if not isinstance(s, str):                    # type guard
        return "invalid"
    s_stripped = s.strip()
    if not s_stripped:
        return "empty"
    if s_stripped.isdigit():                      # all characters digits
        return "numeric"
    if s_stripped.isalpha():                      # all letters
        if s_stripped.islower():
            return "alpha-lower"
        elif s_stripped.isupper():
            return "alpha-upper"
        else:
            return "alpha-mixed"
    # fallback for alphanumeric or other characters
    if any(ch in "!@#$%^&*()" for ch in s_stripped):
        return "contains-symbol"
    return "other"