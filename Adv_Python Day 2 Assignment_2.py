#Single Line Comment:You have a list of email addresses and you want to extract the domain part (the part after '@') from each email address. Example Data:

# Tke Input from user
emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]


# To Extract domain from Email
domains = [email.split("@")[1] for email in emails]


#Dispaly Result
print(domains)


""" OUTPUT

['example.com', 'sample.org', 'mydomain.net']


"""
