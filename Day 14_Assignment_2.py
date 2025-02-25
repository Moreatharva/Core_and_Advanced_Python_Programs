# Single line Comment : Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer


try:
    # Prompting the user for input
    user_input = input("Enter an integer: ")
    
    # Attempting to convert the input to an integer
    number = int(user_input)
    print(f"You entered the integer: {number}")

except ValueError:
    print("Error: This is not a valid integer!")

""" OUTPUT

Enter an integer: 8
You entered the integer: 8



Enter an integer: 3.4
Error: This is not a valid integer!


"""
