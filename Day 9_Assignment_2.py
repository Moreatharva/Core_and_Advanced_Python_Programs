# Single Line Comment:Write a Python program to remove duplicate characters of a given string. 

# Take input from user
s1=input("Enter a string:")

#Split the sentence into  words
s2=s1.split()

#List to store unique words
result =[]  


for word in s2:
    if word not in result:    #if it is not
        result.append(word)

#Join the list back into a sentence
s3=' '.join(result)


#Dislpay thr result
print(s3)


""" OUTPUT

Enter a string:string and string funcion
string and funcion

"""
