# SIngle line Comment:Write a python program finding the factorial of a given number using a while loop

# Take Input from user
num = int(input("Enter a number: "))  
factorial = 1

# Using a while loop to calculate factorial
while num > 0:
    
 # Multiply the current number
    factorial *= num
    
# Decrease the number by 1
    num -= 1  

#Disply the result
print("Factorial:", factorial)
