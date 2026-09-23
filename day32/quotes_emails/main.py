from day32.mailer import *
import random
to_address = "semicolon52@yahoo.com"

# read the quotes
with open('quotes.txt') as file:
    quotes = file.readlines()

random_quote = random.choice(quotes)

send_email(to_address=to_address, message=random_quote, subject="New Quote")

print('Email Sent')