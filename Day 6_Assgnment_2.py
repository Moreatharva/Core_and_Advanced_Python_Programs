#Single Line Comment: Write a python program to check whether a number is palindrome or not?

# Take input from user

num = int(input("Enter a number: "))  
original_num = num  
reversed_num = 0

# Reverse the number
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

# Check if the number is a palindrome

if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")


    
""" OUTPUT

Enter a number: 12345
12345 is not a palindrome.





"""

