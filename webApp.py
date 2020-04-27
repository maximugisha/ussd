from __future__ import print_function

from flask import Flask, request
from flask_restful import Api

import africastalking

app = Flask(__name__)
api = Api(app)


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "sandbox"
        self.api_key = "1578499043ae12ca0f0a9e00070d4ac9cde89ce0a36ee5d7f87bb47011a671ae"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

def send(self):
    # Set the numbers you want to send to in international format
    recipients = ["+256702431725", "14262"]

    # Set your message
    message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

    # Set your shortCode or senderId
    sender = "14262"
    try:
        # Thats it, hit send and we'll take care of the rest.
        response = self.sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()
