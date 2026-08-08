# while Loop: -> The while loop continues executing as long as a condition is True.

# Basic while Loop: -> Simple counter using while loop
count = 1  # Initialize counter

while count <= 5:           # Condition: continue while count <= 5
    print(f"Count is: {count}")
    count += 1              # Increment counter (MANDATORY to avoid infinite loop)

# Output:
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Count is: 5


# while Loop with User Input validation

user_input = ""  # Initialize empty string

# Keep asking until user types 'quit'
while user_input != "quit":  # Condition checks if input is not "quit"
    user_input = input("Enter a command (type 'quit' to exit): ")
    if user_input != "quit":
        print(f"You entered: {user_input}")

print("Goodbye!")


# while Loop with Break Condition: -> Using break to exit early
number = 0

while True:  # Infinite loop (be careful!)
    number += 1
    print(f"Number: {number}")
    
    if number == 5:  # Break condition
        break  # Exits the loop immediately

# Output: 1, 2, 3, 4, 5


# while Loop with Multiple Conditions
# Example 4: While loop with complex conditions
x = 1
y = 10

while x <= 5 and y >= 5:  # Both conditions must be True
    print(f"x={x}, y={y}")
    x += 1
    y -= 2

# Output:
# x=1, y=10
# x=2, y=8
# x=3, y=6
# x=4, y=4 (Loop stops when y >= 5 becomes False)

# 