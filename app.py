from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from coviddateutil import covid_data, covid_data_by_state_and_date
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
        help_msg = "User Manual:\n Available commands: \n\ti)Covid <RTO_PASSING> e.g. Covid MH12 give count of Pune \n\t"+\
        "ii)STATE CODES (Some states in app use slightly different state code, check those by sending message STATE CODES, before firing command (i))\n\t"+\
        "iii)Covid <state_code> <date> <case_category> (To fetch number of cases under particular category for that state on given date. e.g "+\
        "Covid mh 15-May-20 c -> Gives number of confirmed(c:confirmed, r:recovered, a:active, d:deceased cases for Maharashtra on 15-May-20"
        resp.message(help_msg)
    # Create reply
    elif msg.upper() == "STATE CODES":
        state_codes = "(Those not mentioned below follows normal RTO codes) \n1) UT - Uttarakhand \n2) TG - Telangana \n3) OR - Odisha"+\
        "\n4) CT - Chhattisgarh \n5) AR - Arunachal Pradesh" 
        resp.message(state_codes)
    elif msg.upper()[0:5] == "COVID" and len(msg)==10:
        query_data = covid_data(msg.upper())
        resp.message("Data for your query: {}".format(query_data))
    elif msg.upper()[0:5] == "COVID" and len(msg)==22:
        query_data = covid_data_by_state_and_date(msg)
        resp.message("Data for your query: {}".format(query_data))
    else :
        error_msg = "Wrong command"
        resp.message(error_msg)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
