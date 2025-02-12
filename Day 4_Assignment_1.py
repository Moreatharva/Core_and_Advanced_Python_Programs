#  Single line Comment :Python program to check leap year  or not.

#Input year from User
year = int(input("Enter a year: "))
# Leap year is divisible by 4 but not by 100, unless also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
        print("It is not a leap year")

""" OUTPUT

Enter a year: 2004
It is a leap year

Enter a year: 1998
It is not a leap year

"""
