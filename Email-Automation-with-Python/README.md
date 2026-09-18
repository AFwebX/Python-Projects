# Email Automation with Python

A simple email automation program built using Python. This program reads a list of email addresses from a CSV file and sends a randomly selected motivational quote to each recipient.

The program is built using Python fundamentals along with external libraries such as Pandas.

## About the Program

This program automates the process of sending motivational quotes to multiple recipients.

Instead of manually entering each email address, the program reads the email addresses from a CSV file, selects a random quote from a text file, and sends the quote individually to each recipient using Gmail's SMTP server.

## Features in this Program

- Reads email addresses from a CSV file
- Converts the email column into a Python list using Pandas
- Reads motivational quotes from a text file
- Selects a random quote
- Sends emails using Gmail SMTP
- Sends the email individually to each recipient
- Uses `EmailMessage` to create the email
- Checks the date before sending emails

## Technologies Used

- Python
- Pandas
- SMTP
- Gmail SMTP Server

## Python Modules Used

```text
datetime
pandas
smtplib
email
random