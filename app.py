from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from coviddateutil import covid_data
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    resp = MessagingResponse()
    if msg.upper() == "HELP":
        help_msg = "manual:\n Available commands: \n\ti)Covid <RTO_PASSING> e.g. Covid MH12 give count of Pune \n\t"+\
        "ii)State codes (Some states in app use slightly different state code, check those state codes here before firing command (i))"
        resp.message(help_msg)
    # Create reply
    # resp.message("You said: {}".format(msg))
    elif msg.upper() == "STATE CODES":
        state_codes = "(Those not mentioned below follows normal RTO codes) \n1) UT - Uttarakhand \n" 
        resp.message(state_codes)
    elif msg.upper()[0:5] == "COVID" and len(msg)==10:
        query_data = covid_data(msg.upper())
        resp.message("Data for your query {}".format(query_data))
    else :
        error_msg = "Wrong command"
        resp.message(error_msg)
    #, msg, " is ", query_data)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)