#Single line Comment : Python Program to Check if a Number is Positive, Negative or zero


# Input number from the user
num = int(input("Enter the number:"))

# if number is greater tha zero,print positive number
if num > 0:
    print("Positive Number")
    
# if number is less than zero , print negative number
elif num < 0:
    print("Negative Number")

# if number is zero
else:
    print("Zero")


""" OUTPUT

Enter the number:34
Positive Number

Enter the number:-2
Negative Number

Enter the number:0
Zero

"""
