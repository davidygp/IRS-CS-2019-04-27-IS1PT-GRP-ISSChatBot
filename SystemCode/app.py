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
    return "It can be found at:\n Please visit https://www.iss.nus.edu.sg/about-us/getting-to-nus-iss for more info"

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
   else:
       respose_text = "No intent matched"
   # Branching ends here

   # Finally sending this response to Dialogflow.
   return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
