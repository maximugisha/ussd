from __future__ import print_function

from flask import Flask, request
from flask_restful import Api

import africastalking

app = Flask(__name__)
api = Api(app)


class SMS:
    # Set your app credentials
    username = "sandbox"

    api_key = "6f0e59d192c4940953563de43826d9e9a91528400b70b06fad714d7f99337734"

    # Initialize the SDK
    africastalking.initialize(username, api_key)

    # Get the SMS service
    sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["14262", "+256702431725"]

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


@app.route("/", methods=['GET', 'POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", default = '')

    if text == '':
        response = "CON Welcome to Shopto Delivery System \n"
        response += "1. My Account Details \n"
        response += "2. My Latest Transaction \n"
        response += "3. Make an Order "

    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. My Shop number \n"
        response += "2. My Phone Number"

    elif text == '2':
        response = " CON Your Latest Transactions \n "
        response += "1. 2020.04.04 Bidco Oil \n"
        response += "2. 2020.04.04 Akawunga  \n"
        response += "3. 2020.04.04 Fortune Oil "

    elif text == '3':
        if SMS().send():
            response = "END SOME" + phone_number
        else:
            response = "END Encountered an error while sending"

    elif text == '1*1':
        shop_number = "ACC1001"
        response = "END Your Shop Number is " + shop_number

    elif text == '1*2':
        phone_number = "078900035"
        response = "END Your Phone number is " + phone_number
    else:
        response = "END Invalid choice"

    return response


if __name__ == '__main__':
    app.run(debug=True)
