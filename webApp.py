from __future__ import print_function

from flask import Flask
from flask_restful import Api
#Import the AfricasTalking SDK into your app
import africastalking

app = Flask(__name__)
api = Api(app)

#Create your credentials
username = "sandbox"
apikey = "1578499043ae12ca0f0a9e00070d4ac9cde89ce0a36ee5d7f87bb47011a671ae"

# Initialize the SDK
africastalking.initialize(username, apikey)

# Get the SMS service
sms = africastalking.SMS

@app.route('/',methods=['GET', 'POST'])
def sendMessage():
    #Define some options that we will use to send the SMS
    recipients = ['+256702431725', '+256775097505']
    message = 'I\'m a erflumberjack and its ok, I sleep all night and I work all day'
    sender = '14262'

    #Send the SMS
    try:
        #Once this is done, that's it! We'll handle the rest
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"Houston, we have a problem {e}")


sendMessage()
