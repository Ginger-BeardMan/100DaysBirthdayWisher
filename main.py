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
celebrator = random.randint(0, len(birthday_dict)-1)
birthday = f"{birthday_dict[celebrator]['year']}-{birthday_dict[celebrator]['month']}-{birthday_dict[celebrator]['day']}"

# Contact Information
my_email = 'chungus3535@gmail.com'
password = 'abcd1357)('


# ------------------------- Correspondence ------------------------------

# Message
with open()

# Email
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_dict[celebrator]['email'], msg=)

# ------------------- Extra Hard Starting Project ----------------------

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

if birthday == today:
    print('Happy Birthday!')

# 3. If step 2 is true,
# pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
