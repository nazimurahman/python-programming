# SIMPLE while loop - counter example
count = 1                         # count: variable initialized to 1
# while: loop keyword, condition checked before each iteration
while count <= 5:                 # condition: continue while count is less than or equal to 5
    print("Count is:", count)     # print: output current value of count
    count += 1                    # increment count by 1 to eventually stop the loop

print()                           # blank line separator

# while loop with user input and validation
user_input = ""                   # initialize string to hold user input

# Keep asking user until they type 'quit'
while user_input != "quit":       # != : not equal comparison
    # input(): read a line from user, strip() removes leading/trailing whitespace
    user_input = input("Enter a command (type 'quit' to exit): ").strip()
    if user_input != "quit":      # check again to avoid printing after 'quit'
        print("You entered:", user_input)

print("Goodbye!")                 # program exits the input loop

print()                           # blank line separator

# while with break and continue demonstration
number = 0                        # counter variable

while True:                       # True: boolean literal; loop that runs until a break
    number += 1                   # increment
    # demonstrate 'continue' to skip a specific iteration
    if number % 2 == 0:           # %: modulus operator; checks if number is even
        print(number, "is even - skipped further processing in this iteration")
        continue                  # continue: skip to next loop iteration
    print(number, "is odd")
    # break condition to end infinite loop
    if number >= 7:               # >= : greater-than-or-equal comparison
        break                     # break: exit the loop immediately

print("Loop ended at number =", number)

print()

# while loop with multiple conditions and logical operators
x = 1
y = 10

# and: both conditions must be True to enter loop
while x <= 5 and y >= 5:         # multiple conditions combined with 'and'
    print(f"x={x}, y={y}")
    x += 1                       # increment x by 1
    y -= 2                       # decrement y by 2

print()

# Demonstrating comparison operators in real-life contexts
temp_celsius = 30                # example temperature in °C
# if/elif/else: branching that checks conditions in sequence
if temp_celsius < 0:             # '<' cold check
    print("Freezing: below 0°C")
elif temp_celsius <= 18:         # '<=' cool check
    print("Cool: 0–18°C")
elif temp_celsius <= 25:
    print("Comfortable: 19–25°C")
else:                            # else: fallback when no prior condition matched
    print("Warm/hot: above 25°C")

print()

# Membership operators: 'in' and 'not in'
allowed_commands = ["start", "stop", "pause", "quit"]  # list of allowed strings

cmd = "start"
if cmd in allowed_commands:       # 'in' checks membership inside a sequence
    print(cmd, "is an allowed command")

cmd2 = "exit"
if cmd2 not in allowed_commands:  # 'not in' checks non-membership
    print(cmd2, "is NOT an allowed command")

print()

# Identity operators: 'is' and 'is not'
# 'is' checks whether two references point to the same object (identity), not equality
a = [1, 2, 3]
b = a                            # b references same list object as a
c = [1, 2, 3]                    # c is a separate list object with same contents

if a is b:                       # True: same object reference
    print("a is b -> same object")

if a is not c:                   # True: different objects even if contents equal
    print("a is not c -> different objects")

print()

# Chained comparisons: syntactic sugar for readability
value = 15
# checks 10 < value <= 20, same as (10 < value) and (value <= 20)
if 10 < value <= 20:             
    print(value, "is between 11 and 20 inclusive of 20")

print()

# Nested conditionals example (real-world style)
balance = 250.0                  # user bank balance (float)
withdraw_amount = 200.0          # requested withdrawal

# Outer check: is there enough balance overall?
if withdraw_amount <= balance:   # compare requested amount with balance
    # Nested decision: check daily withdrawal limit and minimum remaining balance
    daily_limit = 1000.0
    min_balance = 10.0
    if withdraw_amount <= daily_limit and (balance - withdraw_amount) >= min_balance:
        # perform withdrawal (here we just simulate)
        balance -= withdraw_amount
        print(f"Withdrawal successful. New balance: {balance:.2f}")
    elif withdraw_amount > daily_limit:
        # uses '>' comparison and logical structure to raise an error/notify
        print("Withdrawal denied: exceeds daily limit.")
    else:
        # fallback for insufficient remaining minimum balance
        print("Withdrawal denied: would drop below minimum required balance.")
else:
    print("Withdrawal denied: insufficient funds.")

print()

# Complex condition example using 'or' and 'not'
# Real-life: decide whether to send an alert for a machine based on multiple sensor conditions
temperature = 85                  # degrees
vibration = 0.03                  # g-force
error_flag = False

# 'or' requires any one True to enter; 'not' negates boolean value
if temperature > 80 or vibration > 0.05 or not error_flag:
    # In real systems you'd use parentheses to clarify precedence where needed
    print("ALERT: Check machine (temperature, vibration, or error state triggered)")

print()

# Safe input parsing with while to avoid infinite loops and handle bad input
# Example: ask for an integer between 1 and 10
value = None
while True:
    s = input("Enter an integer between 1 and 10 (or 'quit'): ").strip()
    if s == "quit":
        print("User cancelled input.")
        break
    # try/except: handle invalid integer conversion gracefully
    try:
        value = int(s)            # convert string to integer
    except ValueError:
        print("Invalid integer, try again.")
        continue                  # prompt again without leaving loop
    # Range check using chained comparisons
    if 1 <= value <= 10:
        print("Thank you — valid value:", value)
        break
    else:
        print("Value out of range. Try again.")

print("End of demo.")