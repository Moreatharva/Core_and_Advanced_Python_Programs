#Single Line Comment:Write a python program to reverse a number using a while loop

# Take input from the user 
num = int(input("Enter a number: ")) 
i = 0

while num > 0:
    
# Get the last digit
    remainder = num % 10
    
# Shift digits and add the last digit
    i = (i * 10) + remainder

# Remove the last digit
    num = num // 10  

# Display the Result
print("Reversed Number:", i)

""" OUTPUT

Enter a number: 574923
Reversed Number: 329475

"""
