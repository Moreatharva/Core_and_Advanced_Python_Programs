#Single Line Comment:Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 


def read_file():
    
 # Open the file in read mode
    with open("D:\\New folder\\abc.txt", "r") as file:
        
# Read and print each line
        for line in file:

# strip() removes the newline character
            print(line.strip())  

# Call the function
read_file()


""" OUTPUT

Helloo friends how are you
All the best students for your exam
Hello, World
Python is awesome

"""

