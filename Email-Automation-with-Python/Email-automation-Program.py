import datetime as dt
import pandas as pd
import smtplib
from email.message import EmailMessage
import random

user_email = "afrid.shaik630@gmail.com"
user_password = "abcd efgh ijkl mnop"

df = pd.read_csv("just_emails.csv")

emails = df["Email"].to_list()

with open("quotes.txt") as text:
    quotes = text.readlines()
    quote = random.choice(quotes)

msg = EmailMessage()
msg["From"] = "afrid.shaik630@gmail.com"
msg["Subject"] = "Motivational Quote"
msg.set_content(f"this is a motivational quote for you {quote}")

# msg["to"] = "afrid.shaik630@gmail.com"

my_date = dt.datetime.now().date()

sending_date = dt.datetime.now().date()

print(my_date, sending_date)

if my_date == sending_date: # here we can set date and time to send mails
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_email, password=user_password)
        msg = EmailMessage()
        msg["From"] = "afrid.shaik630@gmail.com"
        msg["Subject"] = "Motivational Quote"
        msg.set_content(f"this is a motivational quote for you : '{quote}' ")

        # msg["to"] = "afrid.shaik630@gmail.com"
       
        for email in emails:
            msg["To"] = email
            connection.send_message(msg=msg)
            del msg["To"]
            print(f"Email sent to {email}")


