from __future__ import print_function
import os
from flask import Flask, request
from flask_restful import Api

import africastalking
app = Flask(__name__)
api = Api(app)

username = os.getenv('user_name', 'sandbox')
api_key = os.getenv('6f0e59d192c4940953563de43826d9e9a91528400b70b06fad714d7f99337734', 'fake')

africastalking.initialize(username, api_key)
sms = africastalking.SMS
airtime = africastalking.Airtime
payment = africastalking.Payment

class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "sandbox"
        self.api_key = "0fd2d64f27622921dba1fc7204073dfaa08be88eac31cae1f683b39f194d0d5b"
        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
        # Get the SMS service
        self.sms = africastalking.SMS


    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+256702431725"]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

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


@app.route("/", methods=['GET', 'POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        response = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number \n"
        response += "3. Send SMS "

    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"

    elif text == '2':
        response = "END Your phone number is " + phone_number

    elif text == '3':
        if SMS.send:
            response = "END SMS Received"
        else:
            response = "END FAILED"

    elif text == '1*1':
        accountNumber = "ACC1001"
        response = "END Your account number is " + accountNumber

    elif text == '1*2':
        balance = "KES 10,000"
        response = "END Your balance is " + balance

    else:
        response = "END Invalid choice"

    return response


if __name__ == '__main__':
    app.run(debug=True)
