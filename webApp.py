from __future__ import print_function

from flask import Flask, request
from flask_restful import Api

import africastalking

app = Flask(__name__)
api = Api(app)

# Create your credentials
username = "sandbox"
apikey = "6f0e59d192c4940953563de43826d9e9a91528400b70b06fad714d7f99337734"

@app.route("/", methods=['GET', 'POST'])
def ussd():
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
        # Send the SMS
        try:
            # Initialize the SDK
            africastalking.initialize(username, apikey)

            # Get the SMS service
            sms = africastalking.SMS

            # Define some options that we will use to send the SMS
            recipients = ['+256702431725', '+256775097505']
            message = 'I\'m a lumberjack and its ok, I sleep all night and I work all day'
            sender = '14262'
            # Once this is done, that's it! We'll handle the rest
            response = "END " + sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f" END Houston, we have a problem {e}")
            response = "END Houston, we have a problem"


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
