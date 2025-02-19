
#Single Line Comment:Write a Python program to Count all letters, digits, and special symbols from the given


# take input from user
input_string = "P@#yn26at^&i5ve"

# Initialize counters
chars = 0
digits = 0
symbols = 0

# Loop through each character in the string
for char in input_string:
    if char.isalpha(): 
        chars += 1
    elif char.isdigit():  
        digits += 1
    else:  
        symbols += 1

# Display the result
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")


""" OUTPUT

Chars = 8
Digits = 3
Symbols = 4

"""
