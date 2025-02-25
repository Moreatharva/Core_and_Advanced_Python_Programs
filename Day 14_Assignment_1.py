# Sigle Line Comment:Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


#Input two Variable

def divide_numbers(a, b):
    try:
    
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("ZeroDivisionError: You cannot Divide by zero.")
    
# Example usage
a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))
divide_numbers(a, b)


""" OUTPUT
Enter numerator: 9
Enter denominator: 0
ZeroDivisionError: You cannot Divide by zero.



Enter numerator: 7
Enter denominator: 8
Result: 0.875


"""
