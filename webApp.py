import os
from flask import Flask, request, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

username = os.getenv('user_name', 'sandbox')
api_key = os.getenv('6f0e59d192c4940953563de43826d9e9a91528400b70b06fad714d7f99337734', 'fake')


@app.route("/", methods=['GET', 'POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        response = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"

    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"

    elif text == '2':
        response = "END Your phone number is " + phone_number

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
