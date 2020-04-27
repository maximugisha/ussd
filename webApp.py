from __future__ import print_function

from flask import Flask, request
from flask_restful import Api

import africastalking

app = Flask(__name__)
api = Api(app)

# Create your credentials
username = "sandbox"
apikey = "6f0e59d192c4940953563de43826d9e9a91528400b70b06fad714d7f99337734"

# Initialize the SDK
africastalking.initialize(username, apikey)

# Get the SMS service
sms = africastalking.SMS

# Define some options that we will use to send the SMS
recipients = ['+256702431725']
message = 'I\'m a lumberjack and its ok, I sleep all night and I work all day'
sender = '14262'


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
        # Send the SMS
        try:
            # Once this is done, that's it! We'll handle the rest
            response = "END " + sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f" END Houston, we have a problem {e}")
            response = "END Houston, we have a problem"


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
