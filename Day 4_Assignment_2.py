# Single line comment :Python Program to Find the Largest Among Three Numbers


# Take in put from the user

#Assignint the three variable form the three number
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))

#if condition
if a >=b and a>=c:
    print("The Largest number is",a)
#elif condition
elif b>=a and b>=c:
        print("The Largest number is", b)
# else condition
else:
    print("The Largest Number is", c)





""" OUTPUT

Enter the number:67
Enter the number:86
Enter the number:75
The Largest number is 86


"""
