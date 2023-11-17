import smtplib
import datetime as dt
import random
import pandas as pd

# ------------------- Data/Starting Information ------------------------

# Date
now = dt.datetime.now()
today = str(now.date())

# Birthday Information
data_file = pd.read_csv('birthdays.csv')
birthday_dict = data_file.to_dict(orient='records')

# Sender Contact Information
my_email = 'chungus3535@gmail.com'
password = 'abcd1357)('

# ------------------------- Correspondence ------------------------------

letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

for person in birthday_dict:
    birthday = f"{person['year']}-{person['month']}-{person['day']}"

    if birthday == today:

        # Message
        with open(f'letter_templates/{random.choice(letter_templates)}', 'r') as b_day_letter:
            letter = b_day_letter.read()
            official_letter = letter.replace('[NAME]', person['name'])
            print(official_letter)

            # Email
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=person['email'], msg=official_letter)

