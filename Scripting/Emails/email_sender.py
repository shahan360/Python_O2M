# Import necessary libraries
import smtplib  # for sending emails using the Simple Mail Transfer Protocol (SMTP)
from email.message import EmailMessage  # to create and structure the email content
from string import Template  # to substitute dynamic content in an email template
from pathlib import Path  # for file handling (can use os.path as an alternative)

# Load the HTML file template using Path and read its content
html = Template(Path('index.html').read_text())  # 'index.html' contains the email's HTML structure

# Create a new EmailMessage object to set up the email content and details
email = EmailMessage()
email['from'] = 'Universe@gmail.com'  # Sender's email address
email['to'] = 'Another_Universe@gmail.com'  # Receiver's email address
email['subject'] = 'Hello There! I hope you are good'  # Subject of the email

# Substitute placeholders in the HTML template with actual content
# Here, the placeholder 'name' in the HTML is replaced with 'Task Master'
email.set_content(html.substitute({'name': 'Task Master'}), 'html')

# Start the process to send the email using Gmail's SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Identifies the client to the server
    smtp.starttls()  # Starts the TLS (Transport Layer Security) encryption for secure email communication
    smtp.login('Universe@gmail.com', 'password')  # Log in to the sender's Gmail account using credentials
    smtp.send_message(email)  # Send the email
    print('All Good Buddy!')  # Confirm that the email was sent successfully

# Note: Gmail requires additional configuration for third-party apps to send emails. 
# Follow this solution for enabling email access:
# https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps

# Learn more about 'pathlib' and why it is useful for file handling:
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

# For more information on how SMTP works:
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/

# Python email library examples:
# https://docs.python.org/3/library/email.examples.html

# MIME Email Handling Package documentation:
# https://docs.python.org/3/library/email.html#module-email
