#Single Line Comment: Write a function in Python to count and display the total number of words in a text file “ABC.txt


def count_words_in_file():
    total_words = 0
    # Open the file in read mode
    with open('D:\\New folder\\abc.txt', 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into words and count them
            words = line.split()
            total_words = total_words + len(words)
    
    # Display the total number of words
    print('Total number of words: ',total_words)

# Call the function
count_words_in_file()

