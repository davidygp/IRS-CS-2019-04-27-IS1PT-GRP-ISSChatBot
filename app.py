from flask import Flask, request, make_response, jsonify
import util

app = Flask(__name__)

# *****************************
# Intent Handlers funcs : START
# *****************************

# ***************************
# Intent Handlers funcs : END
# ***************************
def getLocationIntentHandler():
    return "The Heng Mui Keng Campus can be found at: 29 Heng Mui Keng Terrace, Singapore 119620. Please visit https://www.iss.nus.edu.sg/about-us/getting-to-nus-iss for more info"

def getContactIntentHandler():
    return "For General Enquiries, please email isstraining@nus.edu.sg, For Graduate Programme Enquiries, please email isspostgrad@nus.edu.sg or call 66013161"

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]
    print(req)
 
    if intent_name == "GetLocationIntent" :
        respose_text = getLocationIntentHandler()
    elif intent_name == "GetContactIntent" :
        reponse_text = getContactIntentHandler()
    else:
        respose_text = "No intent matched"

    # Finally sending this response to Dialogflow.
    return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
