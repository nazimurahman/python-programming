"""
Summary:
  -> Comments: Write self-documenting code, use comments for "why" not "what"
  -> Escape Sequences: Use \n for newlines, \t for alignment, raw strings for paths
  -> Print: Use f-strings for formatting, sep/end for control, file= for logging
"""
# Comments

# Single-line comment (most common)

"""
Multi-line comment / docstring
Used for function/class documentation
"""

'''Also valid for multi-line comments'''


#  Escape Sequences - Formatting Output
'''
\n  # New line
\t  # Tab
\\  # Backslash
\'  # Single quote
\"  # Double quote
\r  # Carriage return
\b  # Backspace
\f  # Form feed
\v  # Vertical tab
\a  # Bell/Alert
\ooo # Octal value
\xhh # Hex value
'''


# Print Statement

# Simple print
print("Hello World")

# Multiple arguments (auto-spaced)
print("Value:", 42, "is the answer")

# Custom separator
print("apple", "banana", "orange", sep=", ")

# Custom end character
print("Loading", end="...")
print("Done!")  # Outputs: Loading...Done!

# File output
with open("log.txt", "w") as f:
    print("Error: Connection failed", file=f)