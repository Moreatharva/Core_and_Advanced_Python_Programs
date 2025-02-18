#Single Line comment :Write a Python program to get the largest and smallest number from a list without built in functions.


# Defibe the list
numbers = [10, 4, 35, 2, 88, -5, 13]

# Initialize the first element as both the largest and smallest
largest = smallest = numbers[0]

# Iterate through the list to find the largest and smallest
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Dsilpay the result
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")


""" OUTPUT

The largest number is: 88
The smallest number is: -5

"""
