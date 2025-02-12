 #Single line comment :Declare two variables and print that which variable is largest using ternary operators

# Take user input for two variable

# Enter first number
a=float(input("Enter the first number : "))
#Enter second number
b=float(input("Enter the second number : "))

# Use ternary operator to find the largest number
largest = a if a > b else b


# Print the result
print(f"The largest number is: {largest}")


""" OUTPUT

Enter the first number : 77.0
Enter the second number : 77.1
The largest number is: 77.1

"""
