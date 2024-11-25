# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:01:55 2020

@description: This script sends an SMS message using the Twilio API.
"""

# Import the Twilio Client library
from twilio.rest import Client

# Twilio API credentials (replace with your own credentials from Twilio Console)
# DO NOT hardcode sensitive information in production. Use environment variables instead.
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your Twilio Account SID
auth_token = 'your_auth_token_here'  # Replace with your Twilio Auth Token

# Create a Twilio Client object for authentication
client = Client(account_sid, auth_token)

# Define the message parameters
message = client.messages.create(
    from_='+1234567890',  # Replace with your Twilio phone number
    body='Hello, this is your bot! Good Morning!',  # Message content
    to='+0987654321'  # Replace with the recipient's phone number
)

# Print the unique SID of the sent message as confirmation
print(f"Message sent successfully! Message SID: {message.sid}")



#To further enhance security, you can use environment variables to store sensitive information like account_sid and auth_token. Here's an example:

import os
from twilio.rest import Client

# Fetch credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1234567890',
    body='Hello, this is your bot! Good Morning!',
    to='+0987654321'
)

print(f"Message sent successfully! Message SID: {message.sid}")


# recently in place of Twilio we can use below API to send SMS: https://ntfy.sh/
