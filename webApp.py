from __future__ import print_function

from flask import Flask, request
from flask_restful import Api

import africastalking

app = Flask(__name__)
api = Api(app)

# Create your credentials
username = "sandbox"
apikey = "1578499043ae12ca0f0a9e00070d4ac9cde89ce0a36ee5d7f87bb47011a671ae"

# Initialize the SDK
africastalking.initialize(username, apikey)

# Get the SMS service
sms = africastalking.SMS



@app.route('/sms', methods=['GET', 'POST'])
def sendsms():
    response = ''
    # Define some options that we will use to send the SMS
    recipients = ['+256702431725', '+256775097505', '+815054351311']
    message = 'I want to make an order'
    sender = '14262'

    # Send the SMS
    try:
        # Once this is done, that's it! We'll handle the rest
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"Houston, we have a problem {e}")
    return response


@app.route("/", methods=['GET', 'POST'])
def ussd():
    response = ''
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

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
        sendsms()
        response = "END Your Request to order has been received"

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
