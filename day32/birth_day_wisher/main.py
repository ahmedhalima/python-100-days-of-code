from day32.mailer import *
import random
import datetime
import pandas as pd
# from pathlib import Path
##################### Extra Hard Starting Project ######################

data = pd.read_csv('birthdays.csv')
data_dict = data.to_dict(orient='records')
current_date = datetime.datetime.now()
letters = [
    'letter_1.txt',
    'letter_2.txt',
    'letter_3.txt',
]

def send_birthday_wish(user):
    random_letter = random.choice(letters)
    with open(f'letter_templates/{random_letter}') as file:
        contents = file.read()
        new_content = contents.replace("[NAME]", user['name'])
        send_email(to_address=user['email'], message=new_content, subject="Happy Birth Day")

    # file_path = Path(f'letter_templates/{random_letter}')
    # contents = file_path.read_text()
    # new_content = contents.replace("[NAME]", user['name'])
    # send_email(to_address=user['email'], message=new_content, subject="Happy Birth Day")


for user in data_dict:
    if user['year'] == current_date.year and\
        user['month'] == current_date.month and \
        user['day'] == current_date.day:
        # send email
        send_birthday_wish(user)
